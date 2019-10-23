from phe import paillier
from modular import *
from random import *

import pickle

securityParameter = 128
verbose = False

def getAddShares(procNumber, totalProcs, value, leaderSocket, replySocket, requestSocket, broadSockets = None):
    if procNumber > 0:    #Process is NOT leader
        publicKey = pickle.loads(leaderSocket.recv())
        n = publicKey.n
        if verbose:
            print "Process", procNumber, ":", "Received ", publicKey, "from Leader"
        resp = int(replySocket.recv())
        if verbose:
            print "Process", procNumber, ":", "Received from Process", procNumber-1, ":", resp
        # multiply encrypted input by what we just received
       
        #forwardMessage = (resp*publicKey.encrypt((value%n))) % (n*n)
        forwardMessage = (resp*(value%n)) % (n*n)
        if procNumber < (totalProcs-1):
            requestSocket.send(str(forwardMessage))
            forwardMessage = int(requestSocket.recv())
            if verbose:
                print "Process", procNumber, ":", "Received from Process", procNumber+1, ":", forwardMessage
        # select a random share
        share = generate_share(n)
        leaderSocket.send(str(share)) # send share back to p1
        backMessage = mod_exp(forwardMessage,mod_inv(share,n),(n*n))
        replySocket.send(str(backMessage)); #send something backwards
        prod = int(leaderSocket.recv())    # receive shares
        leaderSocket.send("")
        if verbose:
            print "Process", procNumber, ":", "Received from Leader : ", prod
    
    else:            #Leader Process - Process 0
        shares = [0 for i in range(totalProcs)]
        publicKey, privateKey  = paillier.generate_paillier_keypair()
        # n = publicKey.n
        print "Paillier Keys generated"
        # print n
        #send public key to all parties
        for i in range(totalProcs-1):
            broadSockets[i].send(pickle.dumps(publicKey))
        print "Public key distributed to all parties"
        print "Public key : ", publicKey
        #publicKey.encrypt("10")
        requestSocket.send(str(value))
        #requestSocket.send(str(publicKey.encrypt(10))) #send encrypted x0
        for i in range(totalProcs-1):
            shares[i+1] =  int(broadSockets[i].recv()) # collect all the shares
            if verbose:
                print "Process", procNumber, ":", "Received from Process", i+1, " -- Share :", shares[i+1]
        resp = int(requestSocket.recv())
        if verbose:
            print "Process", procNumber, ":", "Received from Process 1 :", resp
        prod = resp
        #prod = privateKey.decrypt(resp)
        for i in range(1,totalProcs):
            # prod = (prod * shares[i]) % n
            prod = (prod * shares[i])

        for i in range(totalProcs-1):
            broadSockets[i].send(str(prod)); #send product
            broadSockets[i].recv()
        #resp=s_recv(broadSockets[i]);  receive acknowledgement
    # if prod > n/2:
    #     prod = prod-n
    #     #print prod
    return prod
