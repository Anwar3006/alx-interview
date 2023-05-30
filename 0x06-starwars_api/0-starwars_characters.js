#!/usr/bin/node

const request = require('request');

const baseUrl = 'https://swapi.dev/api/films/';

// Function to fetch the characters of a Star Wars movie
const fetchCharacters = (movieID) => {
  if (movieID === undefined) return null;
  const fullUrl = baseUrl + movieID;
  request(fullUrl, (error, response, body) => {
    if (error | response.statusCode !== 200) {
      console.log('Error with request: ', error);
    }

    const convertToJson = JSON.parse(body);
    const characterList = convertToJson.characters;

    characterList.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error | response.statusCode !== 200) {
          console.log('Error with request: ', error);
        }

        const parseToJson = JSON.parse(body);
        const getName = parseToJson.name;
        console.log(getName);
      });
    });
  });
};

// Get Id from Commandline
const getID = process.argv[2];

// pass to function
fetchCharacters(getID);
