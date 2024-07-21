
![Queuing js](https://zupimages.net/up/24/29/qgpn.png)

# Topics covered in this repository :

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue


# Requirements

- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should use the `js` extension


# Required Files for the Project

### `package.json`

Click to show/hide file contents

### `.babelrc`

Click to show/hide file contents

### and…

Run `$ npm install` when you have the `package.json`


# Tasks

### [0. Install a redis instance](./README.md)
* Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/download):


### [1. Node Redis Client](./0-redis_client.js)
* Install node_redis using npm


### [2. Node Redis client and basic operations](./1-redis_op.js)
* In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js). 


### [3. Node Redis client and async operations](./2-redis_op_async.js)
* In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)


### [4. Node Redis client and advanced operations](./4-redis_advanced_op.js)
* In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value


### [5. Node Redis client publisher and subscriber](./5-subscriber.js)
* In a file named 5-subscriber.js, create a redis client:


### [6. Create the Job creator](./6-job_creator.js)
* In a file named 6-job_creator.js:


### [7. Create the Job processor](./6-job_processor.js)
* In a file named 6-job_processor.js:


### [8. Track progress and errors with Kue: Create the Job creator](./7-job_creator.js)
* In a file named 7-job_creator.js:


### [9. Track progress and errors with Kue: Create the Job processor](./7-job_processor.js)
* In a file named 7-job_processor.js:


### [10. Writing the job creation function](./8-job.js)
* In a file named 8-job.js, create a function named createPushNotificationsJobs:


### [11. Writing the test for job creation](./8-job.test.js)
* Now that you created a job creator, let’s add tests:


### [12. In stock?](./9-stock.js)
* Data


# Author  
**Sabrina PAPEAU** - [Github](https://github.com/Holbiwan)
