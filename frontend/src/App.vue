<!--
这个示例展示了如何通过 v-on 指令处理用户输入。
-->

<script setup>
  
  import { ref, reactive } from 'vue'
  import axios from 'axios'
  const message = ref('Hello World!')
  const msg = ref('hello')
  const ans = ref('?')
  function reverseMessage() {
    // 通过其 .value 属性
    // 访问/修改一个 ref 的值。
    message.value = message.value.split('').reverse().join('')
  }
  
  function notify() {
    alert('navigation was prevented.')
  }
  function submit() {
          console.log('111');
          axios.get('/backend/index/', {
            params: {
            'msg': msg.value,
          }
        }).then(res => {
          console.log(res.data);
          ans.value = res.data.ans;
          // ans = res.data.ans;
        }).catch(function (error){
          console.log(error);
          ans.value = error;
        })
      }

  </script>
  
  <template>
    <!--
      注意我们不需要在模板中写 .value，
      因为在模板中 ref 会自动“解包”。
    -->
    <h1>{{ message }}</h1>
  
    <!--
      绑定到一个方法/函数。
      这个 @click 语法是 v-on:click 的简写。
    -->
    <button @click="reverseMessage">Reverse Message</button>
  
    <!-- 也可以写成一个内联表达式语句 -->
    <button @click="message += '!'">Append "!"</button>
  
    <!--
      Vue 也为一些像 e.preventDefault() 和 e.stopPropagation()
      这样的常见任务提供了修饰符。
    -->
    <a href="https://vuejs.org" @click.prevent="notify">
      A link with e.preventDefault()
    </a>
    <form @submit.prevent="submit">
      <input type="text" v-model="msg">
      <input type="submit">
    </form>
    <div>{{ ans }}</div>
    <div>{{ msg }}</div>
  </template>
  
  <style>
  button, a {
    display: block;
    margin-bottom: 1em;
  }
  </style> 