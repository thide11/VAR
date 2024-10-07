<script setup lang="ts">
import { type StyleValue } from 'vue';

defineProps<{
  transcriptionFragments: any
}>()

function toTimeFormat(time : number) {return time.toString().padStart(2, "0")}

function formatTime(timeInSeconds : number) : string {
  const seconds = timeInSeconds % 60
  let minutes = Math.floor(timeInSeconds / 60)

  let output = "";
  if(minutes > 60) {
    const hours = Math.floor(minutes / 60);
    minutes -= hours * 60;
    output = toTimeFormat(hours) + ":";
  }

  output += toTimeFormat(minutes) + ":" + toTimeFormat(seconds);
  
  return output
}

function loadBackgroudImage(transcription : any) : StyleValue {
  console.log(transcription)
  const value = `url("https://meet-indexer.s3.amazonaws.com/${transcription.video_url.replace('videos/', 'thumbnails/').replace('.mp4', '.jpg')}`
  // return `background-image: ${value}"`
  return {
    backgroundImage: value,
    backgroundPosition: "center",
    backgroundSize: "contain",
  }
}

// load();
</script>

<template>

  <div>
    <div v-for="transcriptionFragment in transcriptionFragments" :key="`${transcriptionFragment.id}:${transcriptionFragment.meets_id}`" class="video-container">
      <RouterLink :to="`/meets/${transcriptionFragment.meets_id}?time=${transcriptionFragment.start_time}`" >
        <div class="video-transcription-container">
          <div class="video-bg" :style="loadBackgroudImage(transcriptionFragment)">
            <!-- <h1>{{transcriptionFragment.id}}</h1>
            <h1>Id da reunião: {{transcriptionFragment.meets_id}}</h1> -->
          </div>
          <div class="video-transcription">
            <p id="video-speak">{{transcriptionFragment.transcription}}</p>
          </div>
        </div>
      </RouterLink>
    </div>
  </div>
</template>
<style>

  .video-transcription-container .video-bg {
    margin: 30px;
    width: 700px;
  }

  #video-speak {
    font-style: italic;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  .video-transcription-container {
    width: 100%;
    margin: 20px 0;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
  }

  .video-transcription {
    font-size: 20px;
  }



</style>