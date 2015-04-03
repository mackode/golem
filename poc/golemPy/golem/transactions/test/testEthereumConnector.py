import unittest

import sys
import os

sys.path.append( os.environ.get( 'GOLEM' ) )

from golem.transactions.EthereumConnector import EthereumConnector, EthJSON

sys.path.append( os.environ.get( 'GOLEM' ) )

address = "http://localhost:8080"

class TestEthereumConnector( unittest.TestCase ):
    def testSha3(self):
        dataDesc = EthJSON()
        dataDesc.setMethod("web3_sha3")
        dataDesc.setId(64)
        dataDesc.addParam( "0x68656c6c6f20776f726c64" )
        data = dataDesc.getData()
        ec = EthereumConnector(address)
        self.assertEqual( ec.sendJsonRpc(data), {"id":64, "jsonrpc":"2.0", "result":"0x47173285a8d7341e5e972fc677286384f802f8ef42a5ec5f03bbfa254cb01fad" })

    def testBlock(self):
        dataDesc = EthJSON()
        dataDesc.setMethod("eth_blockNumber")
        dataDesc.setId(83)
        data = dataDesc.getData()
        ec = EthereumConnector(address)
        self.assertGreater( int(ec.sendJsonRpc(data)["result"], 16), 30000)

    def testGetLogs(self):
        dataDesc = EthJSON()
        dataDesc.setMethod("eth_getLogs")
        dataDesc.setId(74)
        dataDesc.addParam({"topics": ["0x12341234"]})
        data = dataDesc.getData()
        ec = EthereumConnector(address)
        print ec.sendJsonRpc(data)

    def testSendTransaction(self):
        ec = EthereumConnector( address)
        self.assertNotIn("error",  ec.sendTransaction(id="0xb60e8dd61c5d32be8058bb8eb970870f07233155", to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
                           gas="0x76c0", gasPrice = "0x9184e72a000", value = "0x9184e72a", data = "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"))



if __name__ == '__main__':
    unittest.main()