//Not For Compilation.
#include <mutex>
#include <streamio>
#include <ofstream>
using namespace std;
class logFile{
    public:
    //Need destructor to close the file.

    //bad constructor 1. 
    // 1. Not thread safe. 
    // 2. and not matter if anything is printted into the logfile, it's always opened.
    logFile() {
        logfile_.open("logfile");
    }

    //Laze initialization. Not open the file in constructor.
    void shared_print (const string &msg) {
        //Bad impl 1. 
        // it's still not thread safe. the file can be opened for multiple times.
        if (!logfile_.is_open()) {
            lock_guard<mutex> lk(mu_file_);
            logfile_.open("logfile");
        }
        //OK impl, but every time when printing, it always try to lock the mu_file_ which is necessary only for the first time.
        {
            lock_guard<mutex> lk(mu_file_);
            if (!logfile_.is_open()) {
                logfile_.open("logfile");
            }
        }
        //Best, using call_once: 
        call_once(flag_, [&]() {logfile_.open("logfile");});


        unique_lock<mutex>(mu_print_, defer_lock);
        logfile_ << msg << endl;

    }


    private: 
    mutex mu_file_;
    mutex mu_print_; 
    ofstream logfile_;
    once_flag flag_;

};