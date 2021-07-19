from base64 import b64encode

def generate_config(context):
    resource = {
        'name': context.properties['name'],
        'type': 'gcp-types/cloudscheduler-v1:projects.locations.jobs',
        'properties': {
            'parent': f"projects/{ context.env['project'] }/locations/{ context.properties.get('region', 'us-central1') }",
            'labels': context.properties.get('labels'),
            'description': context.properties.get('description'),
            'schedule': context.properties['cron'],
            'timeZone': 'America/Sao_Paulo'
        }
    }

    # Se for HTTP
    if 'http' in context.properties:
        resource['properties']['http_target'] = {
            'http_method': context.properties['http']['method'],
            'uri': context.properties['http']['url']
        }

        if 'serviceAccountEmail' in context.properties['properties']['http']:
            resource['properties']['http_target']['oidcToken'] = {
                'serviceAccountEmail': context.properties['http']['serviceAccountEmail']
            }

        if 'payload' in context.properties:
            resource['properties']['http_target']['body'] = b64encode(context.properties['payload'].encode())


    # Se for pubsub
    if 'pubsub' in context.properties:
        resource['properties']['pubsubTarget'] = {
            'topicName': f"projects/{ context.env['project'] }/topics/{ context.properties['pubsub']['topic'] }",
            'data': context.properties.get('payload'),

        }

        if 'payload' in context.properties:
            resource['properties']['pubsubTarget']['data'] = b64encode(context.properties['payload'].encode())

        if 'attributes' in context.properties['pubsub']:
            resource['properties']['pubsubTarget']['attributes'] = context.properties['pubsub']['attributes']

    return { 'resources': [resource] }