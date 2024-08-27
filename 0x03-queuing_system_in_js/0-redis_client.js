import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Reddis Clien Error', err))
  .connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();
