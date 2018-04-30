<template>
  <div id="app">

    <el-row :gutter="20">
      <el-col :span="24"><div class="grid-content ">FreePASA // 免费PascalCoin账户</div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12"><div class="grid-content bg-purple">1. claymore填dpool为stratum+tcp://pasc-asia1.nanopool.org:15555，dwal为"360969.0.您的公钥"并启动矿机数分钟</div></el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light">2. 在验证了您的挖矿能力后，将公钥填入下方，即可获得一个免费PascalCoin账户</div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="8">
        <div>
          <el-input placeholder="" v-model="input">
            <template slot="prepend">公钥：</template>
          </el-input>
        </div>
      </el-col>
      <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="5"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <el-button v-on:click="getpasa">获取免费账户</el-button>
        </div>
      </el-col>
      <el-col :span="5"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
    </el-row>    
  </div>

</template>

<script>
export default {
  data() {
    return {
      input: "",
    }
  },
  mounted(){
    let that = this
    // this.$http.get("/queue")
    // .then(function (resp){
    //   // resp must be int here 
    //   console.log("Init")
    //   // respObj = JSON.parse(resp)
    //   // if (respObj.error) {
    //   // }else{
    //   // }
    //   that.queueNum = respObj
    // })
  },
  getpasa(){
    that = this
    that.$http.get("/getpasa/" + that.input)
    .then(function (resp){
      respObj = JSON.parse(resp)
      if (respObj.error) {
        that.$notify.error({
          title: '发生错误',
          message: respObj.error
        })

      if (respObj.success) {
        that.$notify({
          title: '成功',
          message: respObj.success,
          type: "success"
        })        
      }

    })
    .catch(function (error){
      that.$notify.error({
        title: "发生错误",
        message: JSON.stringify(error)
      })
    })
  }
}
</script>

<style>
#app {
  font-size: 24px;
  /* font-family: Helvetica, sans-serif; */
  text-align: center;
}

.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  font-size: 16px;
  background: #d3dce6;
}
.bg-purple-light {
  font-size: 16px;
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
