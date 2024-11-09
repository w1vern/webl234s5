<script setup>



async function policy() {
  const newWindow = window.open("", "Политика конфиденциальности", "width=800,height=600", "popup");
  newWindow.document.write(`
    <html>
      <head>
        <title>Политика конфиденциальности</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            padding: 20px;
            line-height: 1.6;
          }
          h1 {
            color: #333;
          }
        </style>
      </head>
      <body>
        <h1>Политика конфиденциальности</h1>
        <p>Мы заботимся о защите вашей информации и прилагаем все усилия для обеспечения безопасности личных данных.</p>
        <p>Собранная информация используется исключительно для улучшения качества наших услуг. Ваши данные не будут переданы третьим лицам без вашего согласия, за исключением случаев, предусмотренных законом.</p>
        <p>Для получения дополнительной информации, пожалуйста, свяжитесь с нашей службой поддержки.</p>
      </body>
    </html>
  `)
}

</script>

<template>
  <div class="footer">
    <p class="footer_text">
      © 2024 Гестион. Все права защищены.
    </p>
    <p class="policy" @click="policy">Политика конфиденциальности</p>
  </div>
</template>

<style>
.footer {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: var(--p-surface-200);
  color: var(--p-surface-950);
  border-top: solid var(--p-surface-600) 0.01rem;
}

.footer_text {
  padding: 1rem;
  font-size: 1.2rem;
}

.policy {
  padding: 1rem;

}
</style>