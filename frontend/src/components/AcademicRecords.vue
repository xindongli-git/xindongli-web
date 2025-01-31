<template>
  <div>
    <h1>学术成绩</h1>
    <ul>
      <li v-for="record in records" :key="record.id">
        {{ record.degree }} - {{ record.institution }} ({{ record.year }}): {{ record.score }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      records: []
    };
  },
  created() {
    this.fetchRecords();
  },
  methods: {
    async fetchRecords() {
      const response = await axios.get('/api/academic-records/');
      this.records = response.data;
    }
  }
};
</script> 