COMPILER=/usr/bin/g++
flags=-ggdb -O3 -std=c++11

ifneq (,$(findstring dhvi,$(shell uname -n)))#links and libs for duke cluster
	links=-I/datacommons/dhvi/scripts/lib/boost/ -L /datacommons/dhvi/scripts/lib/boost/ -lboost_filesystem -lboost_system -lboost_serialization -pthread
	libs=/datacommons/dhvi/scripts/lib/boost/boost_1_70_system/lib/libboost_serialization.a
else ifneq (,$(findstring Darwin,$(shell uname -s)))#links and libs for osx
	links=-I/opt/local/include/ #-L/opt/local/include/ -lboost_filesystem -lboost_system -lboost_serialization -pthread
	libs=/opt/local/lib/libboost_serialization-mt.dylib
else #links for linux
	links=-L/usr/lib/x86_64-linux-gnu/ -lboost_filesystem -lboost_system -lboost_serialization -pthread
	libs=/usr/lib/x86_64-linux-gnu/libboost_serialization.a
endif



findCDR: utilities.o main.o
	$(COMPILER)  ${flags} ${links} utilities.o main.o -o findCDR

main.o: main.cpp utilities.hpp
	$(COMPILER) ${flags} ${links} -c main.cpp

utilities.o : utilities.cpp utilities.hpp 
	$(COMPILER) ${flags} ${links} -c utilities.cpp

clean : 
	rm -f *.o

allclean: 
	rm -f findCDR *.o *~
