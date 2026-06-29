In some cases, using your own OAuth credentials may be required. For instance, if you are building a third-party Linux package without access to the OBS Project's API credentials, or if you are a developer who needs to be able to test things locally, potentially for a currently unsupported platform or with new scopes not granted by the OBS Project's credentials/service.

For that purpose, OBS supports changing the OAuth client ids/secrets and service URL via CMake options

Note that OBS does not use an entirely standard OAuth flow for Twitch and Restream, as it uses a proxy that knows the client secret to handle the token exchange, rather than including the secret in the client. The URL of that proxy is set by `OAUTH_BASE_URL` and must be changed to your own if you wish to use your credentials for those services.
  
The server-side OAuth component used by OBS for Twitch and Restream is available here: https://github.com/obsproject/obs-oauth-cf

## CMake Options

Twitch/Restream:
- `OAUTH_BASE_URL` - The base URL for your OAuth server (Note: only visible cmake-gui if "Show advanced" is checked)
- `TWITCH_CLIENTID` - Your Twitch API application Client ID
- `RESTREAM_CLIENTID` - Your Restream API application Client ID
- `TWITCH_HASH`/`RESTREAM_HASH` - Set to "0" (only used for obfuscation in the binary if desired)

**Note:** `OAUTH_BASE_URL` must include a protocol (e.g. `https://`) and trailing slash.

For YouTube the OAuth server is not used, instead, the client id and secret are both directly compiled into the OBS binary:
- `YOUTUBE_CLIENTID` - Your YouTube API application Client ID
- `YOUTUBE_SECRET` - Your YouTube  API application Client secret
- `YOUTUBE_CLIENTID_HASH`/`YOUTUBE_SECRET_HASH` - Set to "0" (only used for obfuscation in the binary if desired)

Omitting a client id/secret and hash pair will disable that service.

## Server-side Implementation Details (Twitch/Restream only)

The required parts of the OBS OAuth implementation are:
1. `<OAUTH_BASE_URL>v1/:platform/redirect` - Redirector
2. `<OAUTH_BASE_URL>v1/:platform/token` - Token Proxy
3. `<OAUTH_BASE_URL>[optional path]` - Redirect URL

The server-side needs to also have access to the `client_secret` and `client_id` for any platforms it supports.

### Redirector

The redirector endpoint simply issues a (temporary) 3XX redirect to the platform's OAuth page (e.g. `https://id.twitch.tv/oauth2/authorize` for Twitch) with the required URL parameters to initiate the OAuth flow.

The target URL includes the Redirect URL (3.), `client_id`, `scope`, and other parameters required by the service in the URL parameters. The `response_type` must be `code`.

Example (taken from the [Twitch OAuth Documentation](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth#authorization-code-grant-flow)):
```
https://id.twitch.tv/oauth2/authorize
    ?response_type=code
    &client_id=hof5gwx0su6owfnys0nyan9c87zr6t
    &redirect_uri=http://localhost:3000
    &scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls
    &state=c3ab8aa609ea11e793ae92361f002671
```

### Token Proxy

The token proxy is sent a POST request with several form parameters, for this purpose you only need to care about `grant_type`, and either `code` if the grant type is `authorization_code` or `refresh_token` if is `refresh_token`.

To complete the flow, the proxy will construct a POST request to the platform's token endpoint that contains the client-supplied `grant_type` and `code`/`refresh_token` as well as the other required parameters such as the `client_secret` and `client_id`. See the specific service's documentation for details.

Example POST body (once again taken from the [Twitch OAuth Documentation](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth#authorization-code-grant-flow)):
```
client_id=hof5gwx0su6owfnys0yan9c87zr6t
&client_secret=41vpdji4e9gif29md0ouet6fktd2
&code=gulfwdmys5lsm6qyz4xiz9q32l10
&grant_type=authorization_code
&redirect_uri=http://localhost:3000
```

### Redirect URL

The redirect URL the user is sent to after completing the authentication process on the platform's side must also start with `OAUTH_BASE_URL` for the OBS client to recognise the flow as having finished and obtain the authorization code from the URL.  
The response body is irrelevant and can be a blank page as the webview should be closed immediately after the redirect occurs and before the page is displayed to the user.
