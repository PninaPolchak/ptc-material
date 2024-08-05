function randomInt(rightBound) {
    return Math.floor(Math.random() * rightBound);
}

function randomString(size) {
    let alphaChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let generatedString = '';
    for (let i = 0; i < size; i++) {
        generatedString += alphaChars[randomInt(alphaChars.length)];
    }

    return generatedString;
}

export default function createRandomObj() {

    let generatedObj = {};

    for (let i = 0; i < 4; i++) {
        let generatedObjField;

        switch (randomInt(5)) {

            case 0:
                generatedObjField = randomInt(1000);
                break;

            case 1:
                generatedObjField = Math.random();
                break;

            case 2:
                generatedObjField = Math.random() < 0.5 ? true : false;
                break;

            case 3:
                generatedObjField = randomString(randomInt(4) + 4);
                break;

            case 4:
                generatedObjField = null;
                break;

            case 5:
                generatedObjField = createRandomObj(fieldCount, allowNested);
                break;
        }
        generatedObj[randomString(8)] = generatedObjField;
    }
    return generatedObj;
}

