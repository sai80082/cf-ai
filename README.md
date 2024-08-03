# Cloudflare Ai Proxy

I made this script mainly targeted for nextlcoud assistant because cloudflare provides Ai endpoints as openai API format for a good number of requests (almost for free) so why not use it instead of hosting our own instance of AI.



### Issue with directly using the cloudflare provided openai API.
Request:
```bash
curl  https://api.cloudflare.com/client/v4/accounts/{accountid}/ai/v1/models \
  -H  "Authorization: Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXX"
```
Response:
```json
{"result":null,"success":false,"errors":[{"code":7001,"message":"GET not supported for requested URI."}],"messages":[]}
```
This is because cloudflare dosen't provide `/v1/models` in their API to solve this i created this script which returns the list of models from the list specified in `main.py` and rest requests are directly passed to the cloudflare API.

## How to use

### 1. Make sure you installed Nexlcoud assistant and openai integration in your nextcloud instance
### 2. Get account id and api key from cloudflare [more info](https://developers.cloudflare.com/workers-ai/get-started/rest-api/#1-get-api-token-and-account-id)
### 3. Docker run

```
docker run -d -e ACCOUNTID=XXXXXXXXXXXX -p 5050:5050 ghcr.io/sai80082/cf-ai:main
```
replace the `XXXXXXXXXXXX` with the account id obtained from cloudflare
### 4. In nextlcoud

- Go to administration settings -> Artificial intelligence
- Under OpenAI and LocalAI integration change
  
  - service url: `http://\<machine-ip>:5050`
    
    change machine-ip to your instace local ip address where this docker container is running.
    ![Alt text](image.png)
  - API key: paste the api key obtained from cloudflare.

 Congratulations now you have AI in your nextcloud instace.

### Note 
Beta models in cloudflare ai dont get counted towards your requests but cloudflare can move them to stable so be careful. you can find all the models [here](https://developers.cloudflare.com/workers-ai/models/#text-generation).

 ### Contributions are welcome!

 Contributions are most welcome like improving the documentation, adding new models to the list,etc

