import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/meteoric-llc-meteoric-llc-default/api/watchmode'

mcp = FastMCP('watchmode')

@mcp.tool()
def list_titles(types: Annotated[Union[str, None], Field(description='Filter result to only include certain types of titles. Pass a single type or pass multiple types comma delimited. Possible values: movie, tv_series, tv_special, tv_miniseries, short_film')] = None,
                regions: Annotated[Union[str, None], Field(description='Pass one of the region values (eg. US), or multiple regions comma delimited to only return sources active in those regions. Currently supported regions: US, GB, CA, AU Note: If you populate the source_ids or source_types you can only set a single region, and if you set no region US will be set by default.')] = None,
                source_types: Annotated[Union[str, None], Field(description='Filter results to only include titles that are available on a specific type(s) of source (such a subscription, or TV Everywhere channel apps, etc). By default all are selected, pass one or multiple (comma delimited) of these values: sub, rent, buy, free, tve Note: If you populate this you can only set a single region, and if you set no region US will be set by default.')] = None,
                source_ids: Annotated[Union[str, None], Field(description='Pass an individual ID for a source (returned from the /sources/ endpoint) to filter the results to titles available on that source. Pass multiple values comma separated to return titles available on one of the sources you pass in. Note: If you populate this you can only set a single region, and if you set no region US will be set by default.')] = None,
                page: Annotated[Union[int, float, None], Field(description="Set the page of results you want to return, if this isn't set you will always get page 1 returned. Default: 1")] = None,
                limit: Annotated[Union[int, float, None], Field(description='Set how many titles to return per page, default and maximum is 250. Default: 250')] = None,
                genres: Annotated[Union[str, None], Field(description='Filter results to only include certain genre(s). Pass in a single genre id (which you would get from the /v1/genres/ endpoint, or multiple comma separated.')] = None,
                sort_by: Annotated[Union[str, None], Field(description='Sort order of results, possible values: relevance_desc, relevance_asc, popularity_desc, popularity_asc, release_date_desc, release_date_asc, title_desc, title_asc. Default value is: relevance_desc.')] = None,
                network_ids: Annotated[Union[str, None], Field(description='Pass an individual ID for a TV network (returned from the /networks/ endpoint) to filter the results to titles the originally aired on that TV network. Pass multiple values comma separated to return titles that aired on one of the networks you passed in.')] = None,
                release_date_start: Annotated[Union[int, float, None], Field(description='Set the start of a range for when the title was released (the initial release of the movie or show, not necessarily when it was released on a streaming service). For example, to only include releases on or after January 1, 2001 set this to 20010101 Default: 20010101')] = None,
                release_date_end: Annotated[Union[int, float, None], Field(description='Set the end of a range for when the title was released (the initial release of the movie or show, not necessarily when it was released on a streaming service). For example, to only include releases on or before December 11, 2020 set this to 20201211 Default: 20201211')] = None) -> dict: 
    '''Get a listing of titles that match certain parameters. This powerful endpoint can allow you to find many combinations of titles. For example you could search for something as granular "Horror Movies Streaming on Netflix in the USA" by using the genres, types, source_ids and regions parameters. Results are paginated, and return 250 pages per query by default. Useful for mapping all Watchmode title IDs in your app, and finding in bulk what titles are available in different countries, different sources or source types. Streaming sources are limited to USA only for free plans.'''
    url = 'https://watchmode.p.rapidapi.com/list-titles'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'regions': regions,
        'source_types': source_types,
        'source_ids': source_ids,
        'page': page,
        'limit': limit,
        'genres': genres,
        'sort_by': sort_by,
        'network_ids': network_ids,
        'release_date_start': release_date_start,
        'release_date_end': release_date_end,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def person(id: Annotated[Union[int, float], Field(description='Default: 7110004')]) -> dict: 
    '''Return details on a specific person (actor, director, etc).'''
    url = 'https://watchmode.p.rapidapi.com/person/7110004'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(search_field: Annotated[str, Field(description='The field for us to search in, either a 3rd party ID or \\\\\\"name\\\\\\" which will search for a movie/show title or a person\'s name depending on the type(s) set. Must be one of the following options: imdb_id, tmdb_person_id, tmdb_movie_id, tmdb_tv_id, name.')],
           search_value: Annotated[str, Field(description='The value we should search for. For example, if you set search_field to imdb_id, this would be the IMDB title/person ID, eg. tt0944947.')],
           types: Annotated[Union[str, None], Field(description='Pass one of the following values, or multiple comma separated values to only return certain types: tv, movie, person.')] = None) -> dict: 
    '''Search for titles or people using an external ID (IMDB, TheMovieDB.org), or by name. Returns an array of results objects, that can either be a title or a person. Useful for getting the Watchmode IDs for titles and people. For example, you can set the parameters to search_value=Breaking%20Bad and search_field=name to get all of the titles named "Breaking bad", and then use the IDs returned in other endpoints such as /v1/title/'''
    url = 'https://watchmode.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search_field': search_field,
        'search_value': search_value,
        'types': types,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete_search(search_value: Annotated[str, Field(description='The phrase to search for, can be a full title or person name, or a partial phrase. For example searching for \\"The sha\\" will find the movie \\"The Shawshank Redemption\\".')],
                        search_type: Annotated[Union[int, float, None], Field(description='Set this to 1 to include titles and people in results. Set this to 2 to include titles only. Set this to 3 to include movies only. Set this to 4 to include TV only. Set this to 5 to include people only. By default this is set to 1. Default: 1')] = None) -> dict: 
    '''Search for titles/and or people by name or a partial name. Useful for building an autocomplete search of titles and/or people. The results include the field result_type to indicate which type of result it is (title or person). For titles, the movie poster will be returned in image_url, for a person a headshot will be returned in image_url.'''
    url = 'https://watchmode.p.rapidapi.com/autocomplete-search'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search_value': search_value,
        'search_type': search_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def streaming_release_dates(start_date: Annotated[Union[int, float, None], Field(description='By default, this endpoint will return release dates from the current date through the next 30 days. Populate this parameter to manually set a start date to include releases from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 20220301')] = None,
                            end_date: Annotated[Union[int, float, None], Field(description='By default, this endpoint will return release dates from the current date through the next 30 days. Populate this parameter to manually set a end date to include releases from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 20220312')] = None,
                            limit: Annotated[Union[int, float, None], Field(description='Set how many release dates to return, default is 500. Default: 250')] = None) -> dict: 
    '''Get a listing of recently released or coming soon releases on the major streaming services. Only major services and US releases dates included, however most of the major services (Netflix, Hulu, etc) release original content on the same days in all countries they support. We return is_original field to indicate wheter the title is an original release on that streaming service.'''
    url = 'https://watchmode.p.rapidapi.com/releases'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def new_titles(start_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a start date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021). Default: 0')] = None,
               end_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a end date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021). Default: 0')] = None,
               page: Annotated[Union[int, float, None], Field(description="Set the page of results you want to return, if this isn't set you will always get page 1 returned. Default: 1")] = None,
               limit: Annotated[Union[int, float, None], Field(description='Set how many titles to return per page, default and maximum is 250. Default: 50')] = None,
               types: Annotated[Union[str, None], Field(description='Filter result to only include certain types of titles. Pass a single type or pass multiple types comma delimited. Possible values: movie, tv_series, tv_special, tv_miniseries, short_film')] = None) -> dict: 
    '''Get a listing of the title IDs of new titles added to Watchmode within the date range. You can use this to find new titles, then use the /v1/title/ endpoint to get details on the title.'''
    url = 'https://watchmode.p.rapidapi.com/changes/new_titles/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'page': page,
        'limit': limit,
        'types': types,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def titles_with_changed_sources(types: Annotated[Union[str, None], Field(description='Filter result to only include certain types of titles. Pass a single type or pass multiple types comma delimited. Possible values: movie, tv_series, tv_special, tv_miniseries, short_film')] = None,
                                regions: Annotated[Union[str, None], Field(description='Pass in the 2 character region code (eg US) for the country you want to get titles with changed sources from. There is a limit to 1 region on this endpoint, if you leave this field blank US changes will be returned only.')] = None,
                                start_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a start date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 0')] = None,
                                end_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a end date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 0')] = None,
                                page: Annotated[Union[int, float, None], Field(description="Set the page of results you want to return, if this isn't set you will always get page 1 returned. Default: 1")] = None,
                                limit: Annotated[Union[int, float, None], Field(description='Set how many titles to return per page, default and maximum is 250. Default: 50')] = None) -> dict: 
    '''Get a listing of titles that have changed to their streaming sources within the date range.'''
    url = 'https://watchmode.p.rapidapi.com/changes/titles_sources_changed/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'regions': regions,
        'start_date': start_date,
        'end_date': end_date,
        'page': page,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def new_people(start_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a start date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 0')] = None,
               end_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a end date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 0')] = None,
               page: Annotated[Union[int, float, None], Field(description="Set the page of results you want to return, if this isn't set you will always get page 1 returned. Default: 1")] = None,
               limit: Annotated[Union[int, float, None], Field(description='Set how many titles to return per page, default and maximum is 250. Default: 50')] = None) -> dict: 
    '''Get a listing of the ids of new people added to Watchmode within the date range.'''
    url = 'https://watchmode.p.rapidapi.com/changes/new_people/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'page': page,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def titles_with_changed_episodes(start_date: Annotated[Union[str, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a start date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values.')] = None,
                                 end_date: Annotated[Union[str, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a end date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values.')] = None,
                                 page: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a end date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021). Default: 1')] = None,
                                 limit: Annotated[Union[int, float, None], Field(description="Set the page of results you want to return, if this isn't set you will always get page 1 returned. Default: 50")] = None) -> dict: 
    '''Get a listing of titles that have changes to their episodes (new episodes, episode details changed, etc) within the date range.'''
    url = 'https://watchmode.p.rapidapi.com/changes/titles_episodes_changed/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'page': page,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def titles_with_changed_details(types: Annotated[Union[str, None], Field(description='Filter result to only include certain types of titles. Pass a single type or pass multiple types comma delimited. Possible values: movie, tv_series, tv_special, tv_miniseries, short_film')] = None,
                                start_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a start date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 0')] = None,
                                end_date: Annotated[Union[int, float, None], Field(description='By default, the changes API will return changes since the beginning of yesterday. Populate this parameter to manually set a end date to include changes from a specific date range, format is YYYYMMDD (eg 20210101 for January 1st, 2021), or for more granular results down to the second YYYYMMDDHHMMSS (eg 20210101123459 for January 1st, 2021 12:24pm and 59 seconds). Hours are in 24 hour format and in Eastern Standard Time. Month, day, hour, minutes and seconds use leading zeros for single digit values. Default: 0')] = None,
                                page: Annotated[Union[int, float, None], Field(description="Set the page of results you want to return, if this isn't set you will always get page 1 returned. Default: 1")] = None,
                                limit: Annotated[Union[int, float, None], Field(description='Set how many titles to return per page, default and maximum is 250. Default: 50')] = None) -> dict: 
    '''Get a listing of titles that have had a change to their basic details (overview, cast, genres, ratings, etc) within the date range.'''
    url = 'https://watchmode.p.rapidapi.com/changes/titles_details_changed/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'start_date': start_date,
        'end_date': end_date,
        'page': page,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def genres() -> dict: 
    '''Return a mapping of genre names and IDs. Some genres have a tmdb_id, which is the corresponding genre ID on TheMovieDB.org API.'''
    url = 'https://watchmode.p.rapidapi.com/genres'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sources(types: Annotated[Union[str, None], Field(description='Pass one of the following values, or multiple comma separated values to only return certain types of streaming sources: sub, free, purchase, tve. \\\\\\"sub\\\\\\" means the service is a subscription service, \\\\\\"tve\\\\\\" means the service is a TV channel app.')] = None,
            regions: Annotated[Union[str, None], Field(description='Pass one of the region values (eg. US), or multiple regions comma delimited to only return sources active in those regions. Currently supported regions: US, GB, CA, AU')] = None) -> dict: 
    '''Return a listing of all streaming sources that Watchmode supports. Optionally filter by type of source (subscription, free, etc).'''
    url = 'https://watchmode.p.rapidapi.com/sources'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'regions': regions,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def networks() -> dict: 
    '''Return a listing of all TV networks that may be returned for a title in the /title endpoint.'''
    url = 'https://watchmode.p.rapidapi.com/networks/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def regions() -> dict: 
    '''Return a listing of all regions (countries) that Watchmode currently supports and their 2 letter country codes used in the return data of other endpoints.'''
    url = 'https://watchmode.p.rapidapi.com/regions/'
    headers = {'x-rapidapi-host': 'watchmode.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
