from useful import *
Terminal.clear()

from multiprocessing import Process, Pipe, Pool

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def g(conn):
    print(conn.recv())

    conn.close()



def start(proc):
    proc.start()

if __name__ == '__main__':
    with Pool(5) as p:
        parent, child = Pipe()
        p0 = Process(target=f, args=(child,))
        p1 = Process(target=g, args=(parent,))
        
        print(p.map(start, [p0, p1]))

        # print(parent.recv())   # prints "[42, None, 'hello']"
        p0.join()
        p1.join()



