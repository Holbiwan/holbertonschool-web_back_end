/* eslint-disable */
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('sendPaymentRequestToApi', () => {
    const sendPaymentWithSinon = sinon.spy(sendPaymentRequestToApi);
    expect(sendPaymentWithSinon(100, 20)).to.deep.equal(
      Utils.calculateNumber('SUM', 100, 20)
    );
    sendPaymentWithSinon.restore;
  });
});
