CXX = g++
CXXFLAGS = -O2 -g -std=c++11 -Wall -Wextra
LDLIBS = -lm

APPL = random_int.exe random_double.exe multiple_distr.exe

all: $(APPL)

%.exe: %.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDLIBS)

clean:
	rm -f $(APPL) *.o core
