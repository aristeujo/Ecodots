"""
Here are some functions which access and manage the Amazon Rekognition system. They have been tested in both Ubuntu and RaspOS.
The AWS Rekognition system works not with images per se, but with vectors, as said in the official documentation:

    Amazon Rekognition doesn't save the actual faces that are detected. 
    Instead, the underlying detection algorithm first detects the faces in the input image.
    For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database. 
    Amazon Rekognition uses feature vectors when it performs face match and search operations using the SearchFaces and SearchFacesByImage operations.

    Source: https://docs.aws.amazon.com/rekognition/latest/dg/API_IndexFaces.html 

So it is not necessary to upload images into the cloud, we only need their facial features saved in a vector. The function that does so is called IndexFaces()
and will be explained further.

These functions do most of what is needed for our purposes. 
Some functions have as parameter a local image path. There are functions in the manageCamera.py module which can handle taking a picture with a USB webcam
connected to the computer and store it just while AWS scans the face.

Most responses from AWS come in the form of a JSON. All of them are detailed in the offical documentation, so in case you need to see all the things it
returns, just refer to it.

The documentation for AWS python SDK is also helpful to understand how the operations work:
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

"""

import boto3
from botocore.exceptions import ClientError
import json
import os


"""
    All the face vectors are stored in a collection and most actions happen inside one. This function creates a new collection with 
    the name given in the parameter collection_id.
    The name of the collection is what we use later to reference it when we need to perform operations.
    The collection is also given an ARN (Amazon Resource Name)

    The function returns the ARN and the statusCode of the operation, such as:
    {
    "CollectionArn": "aws:rekognition:us-east-1:acct-id:collection/examplecollection",
    "StatusCode": 200
    }
"""
def create_collection(collection_id):

    client=boto3.client('rekognition')

    #Create a collection
    print('Creating collection:' + collection_id)
    response=client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')

"""
    This function is used to delete a collection. It takes the existing collection name as an argument and returns the statusCode of the operation.
"""

def delete_collection(collection_id):

    print('Attempting to delete collection ' + collection_id)
    client=boto3.client('rekognition')
    status_code=0
    try:
        response=client.delete_collection(CollectionId=collection_id)
        status_code=response['StatusCode']
        return status_code
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collection_id + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
        status_code=e.response['ResponseMetadata']['HTTPStatusCode']
    return(status_code)

"""
    This function is used to describe a collection, listing how many face vectors it holds. This is mostly useful for checking if a face was actually added.
    It takes the name of the collection as an argument and can return:

        The ARN
        Creation Timestamp 
        The number of faces in the collection 
        The FaceModel version which is the current version used by AWS Rekognition.

"""

def describe_collection(collection_id):

    print('Attempting to describe collection ' + collection_id)
    client=boto3.client('rekognition')

    try:
        response=client.describe_collection(CollectionId=collection_id)
        print("Collection Arn: "  + response['CollectionARN'])
        print("Face Count: "  + str(response['FaceCount']))
        print("Face Model Version: "  + response['FaceModelVersion'])
        print("Timestamp: "  + str(response['CreationTimestamp']))

        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collection_id + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
    print('Done...')


"""
    This function lists all existing collections. the response from AWS returns 2 arrays, one with the existing collections and another one indicating which version of FaceModel
    it is using.

    The function returns the name of existing collections as well as how many there are.
"""
def list_collections():

    max_results=2
    
    client=boto3.client('rekognition')

    #Display all the collections
    print('Displaying collections...')
    response=client.list_collections(MaxResults=max_results)
    collection_count=0
    done=False
    
    while done==False:
        collections=response['CollectionIds']

        for collection in collections:
            print (collection)
            collection_count+=1
        if 'NextToken' in response:
            nextToken=response['NextToken']
            response=client.list_collections(NextToken=nextToken,MaxResults=max_results)
            
        else:
            done=True

    return collection_count  

"""
    This function adds face vectors to a collection. It can take both local images or images stored in an S3 bucket as input.
    The local images must be either .png or .jpg and 64-byte encoded. Luckily for us, python does so automatically.

    It can add multiple faces from the same image. The parameter MaxFaces is set to 1 so it only indexes the biggest face it finds.

    The response it gives can be seen in the AWS Rekognition documentation, as well as additional parameters:
    https://docs.aws.amazon.com/rekognition/latest/dg/add-faces-to-collection-procedure.html

    For the most part, we are only interested in knowing the operation as succesful, but as per the documentation, it can also give us coordinates
    for bounding boxes of the faces it indexed. Whenever a face is indexed, it is given a Face ID, which is a unique number representing that face.
    We can also assign an external ID to it.

"""

def add_faces_to_collection(bucket,photo,collection_id, externalID):

    client=boto3.client('rekognition')

    #If the image is a local image

    with open(photo, 'rb') as image:

        response=client.index_faces(CollectionId=collection_id,
                                    #The code bellow indexes an image from S3.
                                    #Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                    #use the code bellow to pass a local image
                                    Image={'Bytes': image.read()},
                                    ExternalImageId=externalID,
                                    MaxFaces=1,
                                    QualityFilter="AUTO",
                                    DetectionAttributes=['ALL'])

        print ('Results for ' + photo) 	
        print('Faces indexed:')						
        for faceRecord in response['FaceRecords']:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

        print('Faces not indexed:')
        for unindexedFace in response['UnindexedFaces']:
            print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)
        #if image is a local image
        image.close()
        return len(response['FaceRecords'])

"""
    Delete faces from the collection. Arguments is an array of faceIDs of the faces to be deleted
    and the collectionID.
    It returns an array of the deleted faces Id.
"""

def delete_faces_from_collection(collection_id, faces):

    client=boto3.client('rekognition')

    response=client.delete_faces(CollectionId=collection_id,
                               FaceIds=faces)
    
    print(str(len(response['DeletedFaces'])) + ' faces deleted:') 							
    for faceId in response['DeletedFaces']:
         print (faceId)
    return len(response['DeletedFaces'])

"""
    List all faces existing in the collection, arguments are the collectionID and the maximum amount of results.
    Return array with the faces, including their FaceID and their ExternalImageID and bounding boxes.
    Currently set to print only the external Id of the faces.
    To see the complete response, refer to the documentation.
    https://docs.aws.amazon.com/rekognition/latest/dg/list-faces-in-collection-procedure.html
"""    

def list_faces_in_collection(collection_id, maxResults):

    faces_count=0
    tokens=True

    client=boto3.client('rekognition')
    response=client.list_faces(CollectionId=collection_id,
                               MaxResults=maxResults)

    print('Faces in collection ' + collection_id)

 
    while tokens:

        faces=response['Faces']

        for face in faces:
            print (face["ExternalImageId"])
            # print(face)
            faces_count+=1
        if 'NextToken' in response:
            nextToken=response['NextToken']
            response=client.list_faces(CollectionId=collection_id,
                                       NextToken=nextToken,MaxResults=maxResults)
        else:
            tokens=False
    return faces 

"""
    Given a faceId the function searches the collection for other faces matching it with a similarity treshold currently set to 90%.
    The response of this process can better be seen in the official documentation. 
    There is also a maxFaces parameter.
    https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-id-procedure.html
"""

def search_face_in_collection_with_id(face_id,collection_id):
    threshold = 90
    max_faces=2
    client=boto3.client('rekognition')

  
    response=client.search_faces(CollectionId=collection_id,
                                FaceId=face_id,
                                FaceMatchThreshold=threshold,
                                MaxFaces=max_faces)

                        
    face_matches=response['FaceMatches']
    print ('Matching faces')
    for match in face_matches:
            print ('FaceId:' + match['Face']['FaceId'])
            print('imageID' + match['Face']['ImageId'])
            #print('ExternalimageID' + match['Face']['ExternalImageId'])

            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print
    return len(face_matches)

"""
    Quite possibly the main function of this system. Given an image that is either .png or .jpg, it searches the collection for a matching face
    It does not upload the actual image, but the facial vector of it. It returns an array of all the faces that match the simmilarity criteria, currently
    set to 98%.

    To see the complete response, refer to the documentation.
    https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-image-procedure.html

    The imageFile parameter must be the path to an image.

    It can also be configured to use an image on a S3 bucket.
"""

def search_faces_with_image(collection_id, imageFile):

    client=boto3.client('rekognition')
    threshold = 98
    maxFaces=10

    with open(imageFile, 'rb') as image:
  
        response=client.search_faces_by_image(CollectionId=collection_id,
                                    Image={'Bytes': image.read()},
                                    FaceMatchThreshold=threshold,
                                    MaxFaces=maxFaces)
                                    
        faceMatches=response['FaceMatches']
        print ('Matching faces')
        for match in faceMatches:
                print ('FaceId:' + match['Face']['FaceId'])
                print("External Image Id = " + match['Face']['ExternalImageId'])
                print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                print()
    image.close()
    return faceMatches


def main():
    #you can test the functions here

    collection = 'Collection_ecodots'
    Imageid = "EduardoGuimaraesPedrosaFilho"
    faceArray = []

    script_dir = os.path.dirname(__file__)
    photo_path = os.path.join(script_dir, 'pics/temp_image.jpg')

    userFace = search_faces_with_image(collection_id=collection, imageFile=photo_path)[0]['Face']['ExternalImageId']

    print("User face is:", userFace)

    with open("/home/tux/Ecodots/UI/pages/users.json", 'rt') as jsonFile:

        users = json.load(jsonFile)
        print(users)

    
    # with open("/home/tux/Ecodots/UI/pages/users.json", 'wt') as jsonFile:
        
    #     print("modifying")

    #     # users[userFace]['Ecodots'] = 4

    #     users["UsuarioAleatorio"] = {"Name": "Usuário Aleatório", "Ecodots": 3, "ExternalFaceId":"UsuarioAleatorio"}
    #     # jsonFile["UsuarioAleatorio"] = "Usuário Aleatório"

    #     json.dump(users, jsonFile, indent=4, ensure_ascii=False)



    # list_collections()
    # create_collection(collection_id=collection)

    # delete_faces_from_collection(collection_id=id, faces=faces)
    # add_faces_to_collection(bucket,photo,collection_id, externalID=id)



    print("Hello World")
    # faces = list_faces_in_collection("Collection_ecodots", 10)
    # for face in faces:
    #     print(face)
    #     faceArray.append(face['FaceId'])
    
    # print(faceArray)
    # delete_faces_from_collection(collection_id=collection, faces=faceArray)

    #add_faces_to_collection(bucket='ecobucket2021',photo="/home/tux/Ecodots/UI/pics/img3.jpg",collection_id=collection, externalID=Imageid)


if __name__ == "__main__":
    main()