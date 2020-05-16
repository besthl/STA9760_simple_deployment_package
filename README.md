# Lambda Deployment Package

In order to run lambda functions that also manage dependencies, we must leverage a "deployment package", basically a zip file containing your lambda code _and_ all the dependencies it needs all packaged into a single artifact.

This repo provides a few tools that will help you manage your lambda functions and the dependencies.

## Developing

To develop your function:

Build your docker container - when you do this, your requirements.txt will be installed inside the container
```
docker build -t local_lambda .
```

As you make changes, run them like so:

```
docker run -v $(pwd):/app local_lambda python lambda_function.py
```

NOTE: if you want to use a new dependency, you will have to rebuild the container

## Artifact

You want to create a zip file that you can upload to AWS. To do so, run the following:

```
docker build -t deployment -f Dockerfile.deployment_artifact .
```

This builds your zip file.

```
docker run -v $(pwd):/app/artifact deployment
```

This copies the file into your host filesystem so that you can upload it into Lambda.

## Uploading to lambda

![img](https://github.com/mottaquikarim/STA9760_simple_deployment_package/blob/master/assets/Screen%20Shot%202020-05-16%20at%202.42.36%20PM.png?raw=true)

On your Lambda page, click on the left dropdown and pick "Upload...". Make sure that the "entrypoint" of you lambda matches what is provided in that text field. For instance, if your function lives in a file called `function.py` and it is called `main`, then you should update that field to: `function.main`.

Hit "Save" and then if you'd like, once save is complete hit the `Test` button to ensure it works as expected.

## Notes and Assumptions

This assumes you only have a single python file that runs your code. If you wanted to have subfolders, that is all fine but you would need to copy those subfolders into your deployment package. See `Dockerfile.deployment_artifact` and apply the pattern there.

We use the fantastic [docker-lambda](https://github.com/lambci/docker-lambda/blob/master/README.md) project to actually create the artifact. Technically, you can use this container for all of your lambda development needs. Take a look at that git repo for instructions on how to properly test your lambda locally as well.

