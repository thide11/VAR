<script setup lang="ts">

import { getOriginalNode } from 'typescript';
import { ref, onMounted, type VNodeRef } from 'vue';
import { useRoute, useRouter } from 'vue-router';


const route = useRoute()
let video = ref(null) as any;

// onMounted(() => {
//   console.log(video)
//   video.value.currentTime = 10;
//   // video.focus()
// })


console.log(route.params.meetId)
const meetId = route.params.meetId;

const meetData = ref()

async function load() {
  const request = await fetch(`http://localhost:5000/meet/${meetId}`)
  const json = await request.json();

  meetData.value = json;


}

function setCurrentTime() {
  let queryTime = Number(route.query.time);
  console.log(queryTime);
  if(!Number.isNaN(queryTime) && queryTime != 0) {
    video.value.currentTime = queryTime;
    video.value.play();
  }
  console.log(video.value)
}

load();


// function login() { 
//   router.push({ path: 'your-path-here' })
// }


  // const meetId =  $route.params.id;
</script>

<template>

  <div v-if="meetData != null">
    <h1>Video em {{ meetData.video_path }}</h1>
    <video controls :src="meetData.video_url" ref="video" @loadedmetadata="setCurrentTime"></video>
    <h1>Duração: {{ meetData.duration }} segundos</h1>
    <h1>Id: {{ meetData.id }}</h1>
    <h1>Tamanho de {{ meetData.size }} bytes</h1>
  </div>
</template>
<style>
  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  video {
    width: 60%;
  }
</style>