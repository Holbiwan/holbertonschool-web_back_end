/* eslint-disable */
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  it('should return an int number', () => {
    expect(calculateNumber(2.3, 3.1)).to.be.a('number');
  });
  it('should return sum of num', () => {
    expect(calculateNumber('SUM', 2.2, 2, 3)).to.deep.equal(4);
  });
  it('should return sum', () => {
    expect(calculateNumber('SUM', 1, 3)).to.deep.equal(4);
  });
  it('sum of nums', () => {
    expect(calculateNumber('SUM', 1, 1)).to.deep.equal(2);
  });
  it('return sum of nums', () => {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.deep.equal(5);
  });
  it('sum', () => {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.deep.equal(6);
  });
  it('sumNums', () => {
    expect(calculateNumber('SUM', -2, -2)).to.deep.equal(-4);
  });
  it('sum negative', () => {
    expect(calculateNumber('SUM', -1.3, -4.5)).to.deep.equal(-5);
  });
  it('sum decimals', () => {
    expect(calculateNumber('SUM', 0.4, 0.6)).to.deep.equal(1);
  });
  it('sum decimal', () => {
    expect(calculateNumber('SUM', 0.4, 0.2)).to.deep.equal(0);
  });
  it('sum main', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.deep.equal(6);
  });

  it('should return subs of num', () => {
    expect(calculateNumber('SUBTRACT', 2.2, 2, 3)).to.deep.equal(0);
  });
  it('should return sub', () => {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.deep.equal(-2);
  });
  it('sub of nums', () => {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.deep.equal(-3);
  });
  it('return sub of nums', () => {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.deep.equal(-3);
  });
  it('sub', () => {
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.deep.equal(-2);
  });
  it('subNums', () => {
    expect(calculateNumber('SUBTRACT', -2, -2)).to.deep.equal(0);
  });
  it('sub negative', () => {
    expect(calculateNumber('SUBTRACT', -1.3, -4.5)).to.deep.equal(3);
  });
  it('sub decimals', () => {
    expect(calculateNumber('SUBTRACT', 0.4, 0.6)).to.deep.equal(-1);
  });
  it('sub decimal', () => {
    expect(calculateNumber('SUBTRACT', 0.4, 0.2)).to.deep.equal(0);
  });
  it('sub main', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.deep.equal(-4);
  });

  it('should return divs of num', () => {
    expect(calculateNumber('DIVIDE', 2.2, 2, 3)).to.deep.equal(1);
  });
  it('should return div', () => {
    expect(calculateNumber('DIVIDE', 1, 3)).to.deep.equal(0.3333333333333333);
  });
  it('div of nums', () => {
    expect(calculateNumber('DIVIDE', 1, 3.7)).to.deep.equal(0.25);
  });
  it('return div of nums', () => {
    expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.deep.equal(0.25);
  });
  it('div', () => {
    expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.deep.equal(0.5);
  });
  it('divNums', () => {
    expect(calculateNumber('DIVIDE', -2, -2)).to.deep.equal(1);
  });
  it('div negative', () => {
    expect(calculateNumber('DIVIDE', -1.3, -4.5)).to.deep.equal(0.25);
  });
  it('div decimals', () => {
    expect(calculateNumber('DIVIDE', 0.4, 0.6)).to.deep.equal(0);
  });
  it('div decimal', () => {
    expect(calculateNumber('DIVIDE', 0.4, 0.2)).to.deep.equal('Error');
  });
  it('div main1', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.deep.equal(0.2);
  });
  it('div main2', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.deep.equal('Error');
  });
});
