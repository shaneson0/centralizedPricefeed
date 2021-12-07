const TriangleOracle = artifacts.require("TriangleOracle");
const PriceFeed = artifacts.require("PriceFeed");
const symbol = "CFX";
const assertId = "0x65784185a07d3add5e7a99a6ddd4477e3c8caad717bac3ba3c3361d99a978c29";
const price = 0;
const timestamp = Date.now();


module.exports = function (deployer) {
  deployer.deploy(TriangleOracle);


  deployer.then(async () => {
    let TriangleOracleInstance = await TriangleOracle.deployed()
    console.log(TriangleOracleInstance.address)
    
    let Result = await TriangleOracleInstance.putPrice(assertId, price, timestamp)
    console.log(Result)

    await deployer.deploy(PriceFeed);
    let PriceFeedInstance = await PriceFeed.deployed()
    await PriceFeedInstance.initialize(TriangleOracleInstance.address)
    console.log(PriceFeedInstance.address)

  });

};


// Replacing 'TriangleOracle'
// --------------------------
// > transaction hash:    0x13a912a41143b96cabdb68ac42e7ac38b32200d0e2e1be1b99366632f364c6a4
// > Blocks: 10           Seconds: 4
// > contract address:    cfxtest:ace8s16jru09036avv7xtp9s3tad4z68wazn9v995z
// > block number:        54881155
// > block timestamp:     1638880932
// > account:             cfxtest:aate5nxwmdrdavgwjb46ntn3k6zfym9z76s1jckvud
// > balance:             413.394061201958149279
// > gas used:            294052 (0x47ca4)
// > gas price:           0.000000001 GDrip
// > storage collateralized: 0.5625 CFX
// > value sent:          0 CFX
// > total cost:          0.562500000000294052 CFX

// cfxtest:ace8s16jru09036avv7xtp9s3tad4z68wazn9v995z

// Replacing 'PriceFeed'
// ---------------------
// > transaction hash:    0x7ab9f602f5ae033a45033d562aece0daa2bde9a73d04220c1157bfc35324d1e6
// > Blocks: 7            Seconds: 4
// > contract address:    cfxtest:acbye06eytpawj66wu8csz4ffkw5cbu7eu6wrje220
// > block number:        54881175
// > block timestamp:     1638880944
// > account:             cfxtest:aate5nxwmdrdavgwjb46ntn3k6zfym9z76s1jckvud
// > balance:             411.769061201957400923
// > gas used:            706909 (0xac95d)
// > gas price:           0.000000001 GDrip
// > storage collateralized: 1.5 CFX
// > value sent:          0 CFX
// > total cost:          1.500000000000706909 CFX

// cfxtest:acbye06eytpawj66wu8csz4ffkw5cbu7eu6wrje220





























