<script setup>
import { ref, onMounted } from 'vue';
let csrf_token = ref("");


let successMessage = ref("")


function getCsrfToken(){
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
}

onMounted(() => {
    getCsrfToken();
});

function saveMovie()  {
    let form = document.querySelector("#movieForm");
    let formData = new FormData(form);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then((response) => response.json())
    .then(function (data) {
        successMessage.value = 'Movie successfully added!';
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });
};





</script>



<template>
<form @submit.prevent="saveMovie" id="movieForm">
    <div class="form-group mb-3">
        <label for="title" class="form-label">Title:</label>
        <input type="text" name="title" class="form-control" />
    </div>
    <div class="form-group mb-3">
        <label for="description" class="form-label">Description:</label>
        <textarea id="description" name="description" rows="5" class="form-control"></textarea>
    </div>
    <div class="form-group mb-3">
        <label for="poster" class="form-label">Upload Image of Poster:</label>
        <input type="file" name="poster" class="form-control">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>

</form>

</template>