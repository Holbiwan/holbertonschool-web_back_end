/* eslint-disable */
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  let calculateNumberStub, consoleSpy;

  beforeEach(() => {
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber');
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    sinon.restore();
  });

  it('should calculate total using Utils.calculateNumber', function () {
    calculateNumberStub.returns(120);
    sendPaymentRequestToApi(100, 20);
    expect(calculateNumberStub).to.have.been.calledWith('SUM', 100, 20);
    expect(consoleSpy).to.have.been.calledWith('The total is: 120');
  });

  it('should log the correct output to the console', function () {
    calculateNumberStub.returns(130);
    sendPaymentRequestToApi(100, 30);
    expect(consoleSpy).to.have.been.calledWith('The total is: 130');
  });
});
