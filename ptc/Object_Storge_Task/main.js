import { connectToMinIO, createBucket, putObject, listObjects, getObject, updateObjectTags, removeObject } from "./client.js";
import createRandomObj from "./createRandomObj.js";


let minioClient;
let bucketName = "myfirstbucket";
let obj = createRandomObj(minioClient, bucketName);
obj.name = "trial";

export default function () {
    try {
        connectToMinIO(minioClient);
        createBucket(minioClient, bucketName);
        let objID = putObject(minioClient, bucketName, obj);
        let data = listObjects(minioClient, bucketName);
        let object = getObject(minioClient, bucketName, obj);
        updateObjectTags(minioClient, bucketName, obj, { "tag1": "try" });
        removeObject(minioClient, bucketName, obj);
    }
    catch (err) {
        console.log(err);
    }
}
