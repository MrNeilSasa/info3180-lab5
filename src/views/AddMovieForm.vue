<script setup>
import {ref, onMounted} from 'vue'
import MovieForm from '../components/MovieForm.vue';

let movies = ref([])

</script>

<template>
    <div>
        <h1>Add New Movie</h1>
        <MovieForm />
    </div>
</template>