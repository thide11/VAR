<script setup lang="ts">
import { type StyleValue } from 'vue';

defineProps<{
  videos: any
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
function videoUrlPathToDateString(video : any) {
  console.log(video)
  const rawDate = video.video_url.replaceAll("videos/", "").replace(".mp4", "")
  const [hour, rawTime] = rawDate.split(" ");
  if(rawTime != null) {
    const time = rawTime.replaceAll("-", ":");
    const date = new Date(hour + " " + time)
    return date.toLocaleDateString() + " " + date.toLocaleTimeString();
  } else {
    return "Sem data"
  }
}

function loadBackgroudImage(video : any) : StyleValue {
  const value = `url("https://meet-indexer.s3.amazonaws.com/${video.video_url.replace('videos/', 'thumbnails/').replace('.mp4', '.jpg')}`
  // return `background-image: ${value}"`
  return {
    backgroundImage: value,
    backgroundPosition: "center",
    backgroundSize: "cover",
  }
}

// load();
</script>

<template>

  <div class="video-container">
    <div v-for="video in videos" :key="video.id" class="video">
        <RouterLink :to="`/meets/${video.id}`" >
          <div class="video-bg" :style="loadBackgroudImage(video)">
            <!-- <img :src="`url("https://meet-indexer.s3.amazonaws.com/${video.video_url.replace('videos/', 'thumbnails/').replace('.mp4', '.jpg')}`"> -->
            <h1 style="color: transparent;">{{video.video_url.replaceAll("videos/", "")}}</h1>
            <!-- <h1 class="video-time">{{formatTime(video.duration)}}</h1> -->
            <p>
              <!-- {{ `url("https://meet-indexer.s3.amazonaws.com/${video.video_url.replace('videos/', 'thumbnails/').replace('.mp4', '.jpg')}" }} -->

            </p>
          </div>
          <div class="video-metadata">
            <h1>Daily - {{videoUrlPathToDateString(video)}}</h1>
          </div>
        </RouterLink>
    </div>


  </div>
</template>
<style>

  a {
    text-decoration: none;
    color: inherit;
  }

  .video-container {
    display: grid;
    grid-template-columns: auto;
    grid-template-columns: 1fr 1fr 1fr;
    width: 100%;
  }

  .video {
    padding: 10px;
  }

  .video-bg {
    position: relative;
    flex: 1 0 1;
    height: 300px;
    border: 1px solid black;
    padding: 10px;
  }

  .video-bg img {
    width: 100%;
  }

  .video-time {
    position: absolute;
    right: 10px;
    bottom: 10px;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 0 5px;
  }

  .video-metadata {
    font-size: 10px;
  }
</style>