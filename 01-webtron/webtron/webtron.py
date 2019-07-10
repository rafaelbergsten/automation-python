import boto3
import click

session = boto3.Session(profile_name='python')
s3 = session.resource('s3')

@click.group()
def cli():
    "Deploy websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_buckets_objects(bucket):
    "List objects in an s3 buckets"
    for obj in s3.Bucket('postigram-imagem').objects.all():
        print(obj)

if __name__ == '__main__':
    cli()    
