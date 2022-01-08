#!/bin/bash

CONTAINER_NAME="--name="

# Usage info
show_help() {
echo "
Usage: bash ./scripts/build/docker_start.sh
--name container name
-h,--help Show usage
"
}

case $1 in
    "-h" | "--help")
        show_help    # Display a usage synopsis.
        exit
        ;;

    "-n" | "--name")
        echo "Name is: $2"
        CONTAINER_NAME+=$2
        ;;

    *)  # Default case: No more options, so break out of the loop.
    echo "Please provide a container name"
    exit 1
    ;;
esac


VOLUMES="--volume=${PWD}/python:/home/src
         --volume=${PWD}/data:/home/data
         --volume=${PWD}/results:/home/results"
		 

docker run \
-it \
--runtime=nvidia \
--gpus all \
--shm-size 8g \
$VOLUMES \
$CONTAINER_NAME \
perfsales