<script setup>
import { ref, onMounted, toRefs } from 'vue';
let csrf_token = ref("");


let successMessage = ref("");
let errorMessage = ref([]);

let posterInput = ref(null);

const state = toRefs({ posterInput, csrf_token, successMessage, errorMessage });

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

    const title = formData.get('title');
    const description = formData.get('description');
    const poster = state.posterInput.value.files[0];

    let errors = [];

    if (!title || title.trim() === '') {
        errors.push('Error in Title field - This field is required.');
    }

    if (!description || description.trim() === '') {
        errors.push('Error in Description field - This field is required.');
    }

    if (!poster) {
        errors.push("Error in Poster field - A Photo is required in this field.");
    } else {
        const fileType = poster.type;
        if (!(fileType === "image/jpeg" || fileType === "image/png")) {
            errors.push("Poster must be a JPG or PNG image.");
        }
    }

    if (errors.length > 0) {
        errorMessage.value = errors;
        return;
    }

    fetch("/api/v1/movies", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw response;
        }
    })
    .then((data) => {
        successMessage.value = "Movie successfully added!";
        errorMessage.value = [];
        console.log(data);
    })
    .catch((error) => {
        error.json().then((data) => {
            if (data.errors) {
                errorMessage.value = data.errors;
            } else {
                errorMessage.value = ["An unexpected error occurred."];
            }
            successMessage.value = "";
            console.log(data);
        });
    });

};





</script>



<template>
<form @submit.prevent="saveMovie" id="movieForm">
    <div class="alert alert-success" v-if="successMessage">{{ successMessage }}</div>

    <div v-if="errorMessage.length">
      <div class="alert alert-danger" v-for="(error, index) in errorMessage" :key="index">
        {{ error }}
      </div>
    </div>
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
        <input type="file" name="poster" class="form-control" ref="posterInput">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>

</form>

</template>