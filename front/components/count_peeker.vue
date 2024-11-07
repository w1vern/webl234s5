
<script class="setup">
const emit = defineEmits(["increment", "decrement"])

const max_value = defineProps("max_value")

const model_value = defineModel()
const value = ref(0)

function increment(params) {
    if (model_value >= max_value) return
    model_value++
    emit("increment")
}

function decrement(params) {
    if (model_value <= 0) return
    model_value--
    emit("decrement")
}
</script>

<template>
<InputGroup>
	<InputGroupAddon>
		<Button value="-" severity="secondary" @click="decrement"/>
	</InputGroupAddon>
	<InputNumber :v-model="model_value" :min="0" :max="max" :step="1" fluid/>
	<InputGroupAddon>
		<Button value="+" severity="secondary" @click="increment"/>
	</InputGroupAddon>
</InputGroup>
</template>
