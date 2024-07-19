import redis from 'redis';

const client = redis.createClient();

const CHANNEL = 'holberton school channel';

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish(CHANNEL, message, (error, reply) => {
      if (error) {
        console.error(`Failed to publish message: ${error.message}`);
      } else {
        console.log(`Message sent: ${message}, Number of subscribers that received the message: ${reply}`);
      }
    });
  }, time);
};

const run = async () => {
  try {
    await client.connect();
    publishMessage('Holberton Student #1 starts course', 100);
    publishMessage('Holberton Student #2 starts course', 200);
    publishMessage('KILL_SERVER', 300);
    publishMessage('Holberton Student #3 starts course', 400);
  } catch (error) {
    console.error(`Error connecting to Redis: ${error.message}`);
  }
};

run();
