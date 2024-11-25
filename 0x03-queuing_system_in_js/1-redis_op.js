import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Reddis Clien Error', err))
  .connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();

async function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function dislplaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
	if (err) {
	    console.error(err);
	    return;
	}
    });
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');