import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

const app = express();
const port = 1245;

const notFound = { status: 'Product not found' };

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json(notFound);
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  item.currentQuantity = currentStock ?? item.initialAvailableQuantity;

  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  const noStock = { status: 'Not enough stock available', itemId };
  const reservationConfirmed = { status: 'Reservation confirmed', itemId };

  if (!item) {
    res.status(404).json(notFound);
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  currentStock = currentStock ?? item.initialAvailableQuantity;

  if (currentStock <= 0) {
    res.status(400).json(noStock);
    return;
  }

  await reserveStockById(itemId, currentStock - 1);
  res.json(reservationConfirmed);
});
