import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const hsetAsync = promisify(client.hset).bind(client);
const hgetallAsync = promisify(client.hgetall).bind(client);

const data = [
  { key: 'Portland', value: 50 },
  { key: 'Seattle', value: 80 },
  { key: 'New York', value: 20 },
  { key: 'Bogota', value: 20 },
  { key: 'Cali', value: 40 },
  { key: 'Paris', value: 2 },
];

const setHolbertonSchools = async () => {
  try {
    for (const item of data) {
      await hsetAsync('HolbertonSchools', item.key, item.value);
    }
    console.log('All data has been set');
  } catch (error) {
    console.error(`Error setting data: ${error.message}`);
  }
};

const displayHolbertonSchools = async () => {
  try {
    const result = await hgetallAsync('HolbertonSchools');
    console.log(result);
  } catch (error) {
    console.error(`Error retrieving data: ${error.message}`);
  }
};

const run = async () => {
  await setHolbertonSchools();
  await displayHolbertonSchools();
};

run();
