<script setup>
import {ref, onMounted} from "vue";

let movies = ref([]);

function fetchMovies(){
    fetch('api/v1/movies')
        .then((response) => response.json())
        .then((data) => {
            movies.value = data.movies;
        });
}


onMounted(() => {
    fetchMovies();
});


</script>

<template>
    <div class="container">
      <div class="row">
        <div class="col-md-6" v-for="movie in movies" :key="movie.id">
          <div class="card mb-4">
            <div class="row g-0">
              <div class="col-md-4">
                <img :src="movie.poster" class="img-fluid rounded-start" alt="Movie poster">
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h5 class="card-title">{{ movie.title }}</h5>
                  <p class="card-text">{{ movie.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>