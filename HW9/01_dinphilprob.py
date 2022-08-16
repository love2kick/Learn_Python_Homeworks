import threading
import time

class DiningPhilosophers(threading.Thread):
    hungry=True
    def __init__(self, phil, lfork, rfork):
        threading.Thread.__init__(self)
        #forks = threads that will be locked, philosopher = main point
        self.phil=phil
        self.lfork=lfork
        self.rfork=rfork
    
    def run(self):
        while self.hungry:
            lfork, rfork = self.lfork, self.rfork
            time.sleep(2)
            print(f"Philosopher {self.phil} is now hungry and wants to eat!")
            while self.hungry:
                lfork.acquire()
                print(f"Philosopher {self.phil} takes fork {self.phil} on his left.")
                if rfork.acquire(False):
                    lfork.release()
                    print(f"Philosopher {self.phil} puts down fork {self.phil} on his left.")
                    break
                else:
                    print(f"Philosopher {self.phil} takes fork {self.phil+1} on his right.")
                    print(f"Philosopher {self.phil} starts eating.")
                    time.sleep(1)
                    print(f"Philosopher {self.phil} is full.")
                    lfork.release()
                    rfork.release()
                    self.hungry=False
            else:
                return
def dine():
    forks=[threading.Semaphore() for n in range(5)]
    philosophers=[DiningPhilosophers(i, forks[i%5], forks[(i+1)%5]) for i in range(5)]
    DiningPhilosophers.hungry=True
    for d in philosophers:
        d.start()
    time.sleep(10)
    print("Dinner is finished.")
        
if __name__=="__main__":
    dine()