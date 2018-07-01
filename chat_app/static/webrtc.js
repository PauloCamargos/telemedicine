'use strict';

var constraints = {
    video: true
};

var video = document.querySelector('video');

function handleSuccess(stream) {
    video.srcObject = stream;
}

function handleError(error) {
    console.error('getUserMedia error: ', error);
}

navigator.mediaDevices.getUserMedia(constraints).
then(handleSuccess).catch(handleError);