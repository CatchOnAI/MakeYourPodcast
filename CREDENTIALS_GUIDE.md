# 🔐 阿里云凭证配置指南

## 问题原因

您的脚本缺少阿里云 API 的访问凭证（Access Key）。

## 📝 需要申请什么

需要两个密钥：

1. **Access Key ID** - 访问密钥 ID（类似用户名）
2. **Access Key Secret** - 访问密钥（类似密码，只显示一次）

## 🌐 在哪里申请

### 选项 1: RAM 控制台（推荐）

1. 访问：https://ram.console.aliyun.com/users
2. 点击 **用户** → **创建用户**（或使用已有用户）
3. 勾选 **OpenAPI 调用访问**
4. 创建后点击用户名
5. 点击 **创建 AccessKey**
6. **立即保存** AccessKey ID 和 Secret（只显示一次！）

### 选项 2: 用户中心快速入口

直接访问：https://usercenter.console.aliyun.com/#/manage/ak

## ⚙️ 配置方法（3选1）

### 方法 1: 使用配置脚本（最简单）✨

```bash
bash configure_credentials.sh
```

脚本会：
- 提示输入 Access Key ID 和 Secret
- 自动创建配置文件
- 设置环境变量
- 提供永久配置建议

### 方法 2: 手动设置环境变量（临时）

在终端运行：

```bash
# 设置环境变量
export ALIBABA_CLOUD_ACCESS_KEY_ID="你的AccessKeyId"
export ALIBABA_CLOUD_ACCESS_KEY_SECRET="你的AccessKeySecret"

# 验证
echo $ALIBABA_CLOUD_ACCESS_KEY_ID

# 运行脚本
python create_podcast.py
```

**对于 Fish Shell（您当前使用的）：**

```fish
set -gx ALIBABA_CLOUD_ACCESS_KEY_ID "你的AccessKeyId"
set -gx ALIBABA_CLOUD_ACCESS_KEY_SECRET "你的AccessKeySecret"

# 运行脚本
python create_podcast.py
```

### 方法 3: 创建配置文件（永久）

```bash
# 创建目录
mkdir -p ~/.alibabacloud

# 创建配置文件
nano ~/.alibabacloud/credentials.ini
```

文件内容：

```ini
[default]
type = access_key
access_key_id = 你的AccessKeyId
access_key_secret = 你的AccessKeySecret
```

保存后直接运行脚本即可。

## 🐟 Fish Shell 永久配置

编辑 `~/.config/fish/config.fish`：

```bash
nano ~/.config/fish/config.fish
```

添加：

```fish
# Alibaba Cloud Credentials
set -gx ALIBABA_CLOUD_ACCESS_KEY_ID "你的AccessKeyId"
set -gx ALIBABA_CLOUD_ACCESS_KEY_SECRET "你的AccessKeySecret"
```

重新加载：

```fish
source ~/.config/fish/config.fish
```

## 🔒 安全最佳实践

### ✅ 应该做的

- ✅ 使用 RAM 子账号（不要用主账号）
- ✅ 只授予必要的权限（最小权限原则）
- ✅ 定期轮换 Access Key
- ✅ 使用配置文件或环境变量，不要硬编码
- ✅ 将凭证文件添加到 `.gitignore`

### ❌ 不应该做的

- ❌ 不要把 Access Key 提交到 Git
- ❌ 不要分享给他人
- ❌ 不要在代码中硬编码
- ❌ 不要使用主账号的 Access Key

## 🎯 需要的权限

确保您的 Access Key 有以下权限之一：

**方案 1: 使用系统策略（简单）**
- `AliyunAIPodcastFullAccess` - AI 播客完全访问权限

**方案 2: 自定义策略（精细控制）**
```json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aipodcast:PodcastTaskSubmit",
        "aipodcast:GetPodcastTask"
      ],
      "Resource": "*"
    }
  ]
}
```

## 📋 配置检查清单

申请和配置完成后，检查：

- [ ] 已获得 Access Key ID（20位左右）
- [ ] 已获得 Access Key Secret（30位左右）
- [ ] 已保存到安全的地方
- [ ] 已配置环境变量或配置文件
- [ ] 已授予 AI Podcast 权限
- [ ] 已添加 `.alibabacloud/` 到 `.gitignore`
- [ ] 可以成功运行测试脚本

## 🧪 测试配置

配置完成后测试：

```bash
# 1. 检查环境变量
echo $ALIBABA_CLOUD_ACCESS_KEY_ID
# 应该显示您的 Access Key ID

# 2. 检查配置文件
cat ~/.alibabacloud/credentials.ini
# 应该显示配置内容

# 3. 运行测试脚本
python create_podcast.py
# 应该成功提交任务
```

## 🐛 常见问题

### Q: Access Key 在哪里查看？
A: 创建时只显示一次！如果忘记了，需要重新创建新的。

### Q: 提示权限不足？
A: 在 RAM 控制台为用户添加 `AliyunAIPodcastFullAccess` 策略。

### Q: 环境变量不生效？
A: 
- 确保没有拼写错误
- 重新启动终端
- Fish Shell 使用 `set -gx`，不是 `export`

### Q: 配置文件路径是什么？
A: `~/.alibabacloud/credentials.ini` 或 `~/.aliyun/config.json`

### Q: 如何撤销 Access Key？
A: 在 RAM 控制台找到对应的 AccessKey，点击禁用或删除。

## 📞 获取帮助

- 阿里云文档：https://help.aliyun.com/document_detail/378659.html
- RAM 访问控制：https://ram.console.aliyun.com
- 工单支持：https://workorder.console.aliyun.com

## 🚀 配置完成后

配置好后，运行：

```bash
python create_podcast.py
```

应该看到：

```
╭─────────────────────────────────────╮
│ AI Podcast Creator                  │
│ Powered by Alibaba Cloud AI Podcast │
╰─────────────────────────────────────╯

Submitting podcast task...
✓ Done!

┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field      ┃ Value                ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ Task Id    │ task-xxxxx           │
│ Request Id │ req-xxxxx            │
└────────────┴──────────────────────┘
```

祝您使用愉快！🎉


