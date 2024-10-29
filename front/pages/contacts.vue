<script setup>

</script>

<template>
    <div class="page">

        <Header></Header>
        <div class="content_with_footer">
            <div class="content">


            </div>
            <Footer></Footer>
        </div>
    </div>
</template>

<style scoped>
.page {
    min-height: 100vh;
}

.content_with_footer {
    display: flex;
    flex-direction: column;

    height: 100vh;
}

.content {
    flex-grow: 1;
}
</style>