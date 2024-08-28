import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', function() {
  before(() => {
    kue.Job.testMode.enter();
  });

  beforeEach(() => {
    return kue.Job.removeAll();
  });

  after(() => {
    kue.Job.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs and add them to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobIds = kue.Job.testMode.jobs.map(job => job.id);

    expect(jobIds).to.have.lengthOf(jobs.length);
    expect(jobIds).to.include.members([1, 2]);
  });
});
