# secret-santa

Simple console application which takes a list of people (with email addresses)
and associates them into giver-receiver pairs. The results will be emailed to 
the participants. This might be used to coordinate an event such as 
[Secret Santa](https://en.wikipedia.org/wiki/Secret_Santa).

## Configuration
The application can be configured with the _config.py_ file. 

## Participants File
The event participants are contained in _people.csv_, which has the following
format:

person1Name,person1Email
person2Name,person2Emai1
person3Name,person3Emai1

So, for example

Marty,mcfly227@example.com
Jennifer,jparker@example.com
Emmett,docbrown@example.com

would represent the following table:

|Name    |Email               |
|--------|--------------------|
|Marty   |mcfly227@example.com|
|Jennifer|jparker@example.com |
|Emmett  |docbrown@example.com|

## Excluding Certain Pairs

Sometimes you may want to exclude pairs of people, for example, friends or
couples who will already be getting each other a gift. These pairs are 
defined in the _exclusions.csv_ file.
