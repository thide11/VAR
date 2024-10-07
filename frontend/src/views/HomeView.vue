<script setup lang="ts">
import VideoList from '../components/VideoList.vue'
import { ref, watch, onMounted } from 'vue';
import VideoTranscriptionList from '../components/VideoTranscriptionList.vue';

interface Video {
  id : number,
  duration : number,
  video_url : string,
}

interface TranscriptionFragment {
  id : number,
  meets_id : number,
  transcription : string,
  video_url : string,
}

const baseUrl = "http://localhost:5000";

let message = ref("");
let search = ref("");

onMounted(async () => {
  try {
    const request = await fetch(baseUrl)
    const json = await request.json();

    if(json?.length <= 0) {
      message.value = "Não foi encontrado nenhum vídeos transcrito";
    }

    videos.value = json;
    console.log(json)
  } catch (e) {
    message.value = "Erro ao buscar vídeos, verifique se o servidor está rodando"
    console.log(e)
  }
});

watch(search, (newValue, old) => {
  searchTranscription(newValue)
})

// videos

const videos = ref<Video[]>([
//   {
//   id: 1,
//   duration: 10,
//   video_url: "",
// }
]);

const searchTranscriptionFragments = ref<TranscriptionFragment[]>([{
  id: 1,
  meets_id: 2,
  transcription: "",
  video_url: "",
}]);

async function searchTranscription(a : string) {
  try {
    const request = await fetch(`${baseUrl}/search/${a}`)
    const json = await request.json();
    searchTranscriptionFragments.value = json.slice(0, 100);
    console.log(json)

  } catch (e) {
    // console.log(e)
  }

  // console.log(a)
}

</script>

<template>
  <main class="container">
    <input id="search" type="text" v-model="search" placeholder="Pesquisar por algo dito na reunião" :on-change="searchTranscription" v-if="videos?.length > 0">
    <VideoList :videos="videos" v-if="search == ''"/>
    <p v-if="message != null" id="message">{{message}}</p>
    <VideoTranscriptionList :transcription-fragments="searchTranscriptionFragments" v-if="search != ''"></VideoTranscriptionList>
  </main>
</template>
<style>
  #message {
    margin-top: 20px;
    font-size: 32px;
  }

  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    align-items: center;
  }

  #search {
    margin-top: 50px;
    width: 50%;
    padding: 15px;
    font-size: 25px;
  }
</style>