import spotipy
from cloudfn.http import Response

token = "BQDXtTvT1SlP_2mex2qP9WqReXCL8WheQaAv5swC9JyiDLfRlIfsYSW2UpDtRyw_OEbRHSDfDehDjJP3Fulhxtt-rmIdRywjYh0UvhStsE4zimR0QitnFHEliBjHMpSTFlX13g1JzxJk"

spotify = spotipy.Spotify(auth=token)

def get_music_suggestions(request):
  	#get sound cloud client
    request_json = request.get_json()
    if request_json and 'query' in request_json:
        results = spotify.search(q=request_json['query'])
        return Response(
            status_code=200,
            body={'data': results},
            headers={'content-type': 'application/json'},
        )
    else:
        return f'Give a query.'
