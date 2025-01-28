## Mamas Kitchen:

### How to run:
In order to run Mama's Kitchen you will need to have docker and docker-compose installed. 

Run `docker compose -f 'docker-compose.yml' up -d --build `
> If you want to see logs you can omit the "-d"


### Tasks

#### Backend
- [] Add Go Logging 
- [] Add Python Logging
- [] add error handling for python
- [] add error handling for golang
- [x] Create a InMemory Recipe Store to serve to the UI
- [x] local upload to blob store
- [x] local enqueue message
- [x] build worker(python) to pull message
- [x] transcribe locally
- [] transform locally
- [] connect to a database(mongo)



#### Frontend
- [x] Create a Logo with a link to the grid view
- [x] upload component to upload audio files
- [] record audio and upload it to storage.
- [] style the page to make it look good
- [] search page


#### Clean up Tasks
- [x] restructure the code
- [] add linters and formatters to auto check during build
- [x] use docker to build frontend and a script to tie it in with go binary
- [x] add cmd folder
- [x] build scripts - docker compose
- [x] upload to github
- [] use cloud prod envs

