const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

///////Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

///////Initialize variables
let reservationEnabled = true;

///////Queue
const queue = kue.createQueue();

//////Function to set the number of availble seats
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

////// function to set the number of available seats
async function getCurrentAvailableSeats() {
    const seats = await getAsync("available_seats");
    return parseInt(seata, 10);
}
reserveSeat(50);

app.get('/available_seats', async (req, res) => {
    if (!reservationEnabled) {
	return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
	if (err) {
	    return res.json({ status: 'Reservation failed' });
	}
	res.json({ status: "Reservation failed" });
    });

    job.on('complete', () => {
	console.log('Seat reservation job ${job.id} completed');
    });
    job.on('failed', (err) => {
	console.log('Seat reservation job ${job.id} failed: ${err.message}');
    });
});

////// Route to process the queue
app.get('/process', (req, res) => {
    res.json({ status: "Queue processing" });

    queue.process('reserve_seat', async (job, done) => {
	const availableSeats = await getCurrentAvailableSeats();

	if (availableSeats > 0) {
	    await reserveSeat(availableSeats - 1);
	    if (availableSeats - 1 === 0) {
		reservationEnabled = false;
	    }
	    done();
	}else {
	    done( new Error('Not enough seats available'));
	}
    });
});

///// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
