<template>
  <div id="app">

    <el-row :gutter="20">
      <el-col :span="24"><div class="grid-content ">FreePASA // 免费PascalCoin账户</div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12"><div class="grid-content bg-purple">1. claymore填dpool为stratum+tcp://pasc-asia1.nanopool.org:15555，dwal为"7711.0.您的公钥"并启动矿机数分钟</div></el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light">2. 在验证了您的挖矿能力后，将正确的公钥填入下方并点击确定，成功提示后数分钟即可获得一个免费PascalCoin账户。</div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="2"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="12">
        <div class="grid-content">
          每个公钥（每人）只可领取一次，恶意行为ip及其获取账户将被曝光在社区与媒体
        </div>
      </el-col>
      <el-col :span="2"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
    </el-row>   
    <el-row :gutter="20">
      <el-col :span="3"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="18">
        <div>
          <el-input placeholder="" v-model="input">
            <template slot="prepend">公钥：</template>
          </el-input>
        </div>
      </el-col>
      <el-col :span="3"><div class="grid-content bg-purple"></div></el-col>
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
        <div class="grid-content">
          <el-button v-on:click="getpasa()">获取免费账户</el-button>
        </div>
      </el-col>
      <el-col :span="5"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6"><div class="grid-content bg-purple-light"></div></el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          捐赠PASC: 7711-71
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple-light">
          捐赠PASA: <a v-on:click="servicePubKey">点击获取公钥</a>
        </div>
      </el-col>
      <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
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
    //   // resp.data = JSON.parse(resp)
    //   // if (resp.data.error) {
    //   // }else{
    //   // }
    //   that.queueNum = resp.data
    // })
  },
  methods: {
    getpasa: function (){
      console.log("start getpasa")
      var that = this
      that.$http.get("/getpasa/" + that.input)
        .then(function (resp){          
          if (resp.data.error) {
            that.$notify.error({
              title: '发生错误',
              message: resp.data.error
            })
          }

          if (resp.data.success) {
            that.$notify({
              title: '成功',
              message: resp.data.success,
              type: "success"
            })        
          }
        })
        .catch(function (error){          
          that.$notify.error({
            title: "发生错误",
            message: error
          })
        })
    },
    servicePubKey: function (){
      var host_pubkey = "3GhhbonhKfpLAZYurzU2TAbiCF2gjSgyx896sTKVVLRp8jCZY9ehUuDsZLzT5DVNAdH98Co62v3PEv5yYLR7xsHcCULmy236ir6xwt"
      if (event.clipboardData) {
        return event.clipboardData.setData("text/plain", host_pubkey);  
      } else if (window.clipboardData) {
        return window.clipboardData.setData("text", host_pubkey);  
      }
      this.$alert('秘钥: 3GhhbonhKfpLAZYurzU2TAbiCF2gjSgyx896sTKVVLRp8jCZY9ehUuDsZLzT5DVNAdH98Co62v3PEv5yYLR7xsHcCULmy236ir6xwt', '已成功复制到粘贴版', {
        confirmButtonText: '确定'
      });
    }
  }

}
</script>

<style>
#app {
  font-size: 18px;
  /* font-family: Helvetica, sans-serif; */
  text-align: center;
}

.el-row {
  margin-bottom: 22px;
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

.el-message-box {
  width: 1111px;
}
</style>
