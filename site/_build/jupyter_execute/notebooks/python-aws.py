#!/usr/bin/env python
# coding: utf-8

# # AWS & Python

# From data storage to computing, Amazon Web Services is a scalable and and cost effective alternative to on premise options. This guide demonstrates how Urban Institute researchers can use Python in conjunction with Amazon Services S3 and EC2 to create a cloud based workflow. 

# ## S3

# Boto3 is the Amazon Web Services SDK for Python with an easy to use, well documented [API](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). It allows one to write Python code that interacts with AWS. In this guide we will explore specifically how Boto3 can be used to interact with AWS S3, Simple Storage Service. 
# 
# S3 can be used to store big data for a relatively small price. It is essentially a file storage system, consisting of buckets, which are analogous to folders. You can use Boto3 to place files into buckets and download files that are stored in buckets, among other actions. In the context of a research model or script, this means you can store and read in input files from S3 and write output files to S3. 
# 
# 
# 
# ### Setting up

# Getting started with Boto3 involves installing Boto3 and authenticating yourself using your AWS credentials as described in this quickstart [guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html). The most secure way to do so is by setting up your credentials file using the Amazon Command Line Interface. In order to do this, you will need your own access key and access key ID. In order to set up a role with the permissions you need, you should contact the tech team.

# ### Running Boto3 Commands

# Using Boto3, there are multiple classes that will allow interaction with S3. In this guide we will use the Resource class, which is a high level, object oriented interface to AWS. 
# 
# First, we will instantiate a service resource which represents the Amazon S3 service. 
# 
# In order to view all of the buckets that are associated with your AWS S3 account, you can run the below code. If your desired bucket is not there, contact the tech team to adjust the permissions associated with you account.
# 
# ```
# import boto3
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
# ```

# Next you can instantiate a bucket resource representing your desired bucket. This will allow you to interact with the bucket. The code below demonstrates using an instantiated bucket to download a file from S3:
# 
# ```
# mybucket = s3.Bucket('mybucket')
# mybucket.download_file('example.txt', '/tmp/example.txt')
# ```
# 
# And upload a file to S3:
# 
# ```
# mybucket.upload_file('/tmp/example.txt', 'example.txt')
# ```

# For a full list of operations you can perform on your bucket, refer to this [documentation]( https://boto3.amazonaws.com/v1/documentation/api/1.9.96/reference/services/s3.html#bucket). Keep in mind that your  will need to have specific permission associated with your account to perform any action.
# 
# ### S3 Triggers
# S3 can be used to trigger AWS events relating to other services. For example an S3 bucket can be configured so that when a file is placed into it:
# * An email is sent to a user
# * An EC2 instance spins up and runs a script which takes in that file as input
# 
# Contact the tech team if you would like to set up a trigger for your S3 bucket. 

# ## EC2

# EC2 is an amazon service which provides compute capacity in the cloud. Rather than running your models and scripts on Urban on premise servers, you can run them on EC2 which provides customizable compute capacity, memory, and more. 
# 
# ### Using tech-tools to spin up an EC2 instance
# 
# The tech team at Urban has designed a tool for researchers to easily create and terminate EC2 instances. This tool is hosted on the tech-tools site via the Urban Institute intranet page. 
# 
# To begin, under the **Research Platforms** dropdown on the tech-tools site, select **Start or Stop EC2 instance**. In order to spin up your EC2 instance, you will be able to select which instance type you would like based on your specific needs and submit the form. 

# ![title](img/tech-tools.png)

# After your instance has spun up, you will receive an email which contains links that point your browser to Jupyter or RStudio on your instance. You can also use your instance's IP to SSH into it. When you are finished with the instance, you can terminate it, and you will be charged only for the amount of time that it was running. 
# 

# ## Putting it all together

# S3 and EC2 can be used to create a workflow entirely hosted in the cloud. The tech-tools site simplifies the process of working with EC2, abstracting many details of the creation and termination away from the user. In terms of more complex workflows using EC2 and other services, the Technology and Data team can partner with your team for design and implementation. in order to create more complex workflows. An example workflow fpr a Python data processing script is detailed below.
# 
# As mentioned earlier, a rule can be set so that the placement of a file into an S3 bucket triggers the creation of an EC2 instance. This workflow begins with an input data file being placed into an input S3 bucket via Boto3. This triggers an EC2 instance to spin up, obtain the input file, and run the data processing script. At the end of the run, the output file is written to the output S3 bucket, and the EC2 instance automatically terminates. Additionally, a rule is set on the output bucket to trigger a notification of the user when a file is placed into it.

# ![title](img/aws-workflow.png)

# This and similar workflows have been employed by the Urban Institute Tech and Data team to run data processing scripts and research models, including the TPC Tax Calculator and the Social Genome Model. Both of the models use Boto3 to place and retrieve objects in S3, and the Social Genome Model written in Python because of Python's compatibility with the EC2 server.
