#!/usr/bin/env node
//Setup Pins
var ServoPinF1 = <Pin>;
var ServoPinF2 = <Pin>;
var ServoPinF3 = <Pin>;
var ServoPinF4 = <Pin>;
var ServoPinF5 = <Pin>;

var ServoPinE1 = <Pin>;
var ServoPinE2 = <Pin>;

var ServoPinH1 = <Pin>;

var LEDPin = <Pin>;

//Set ms count for Servos
var HundertAchtzig = <count>;
var Neunzig		   = <count>;
var Null		   = <count>;

var blynkToken = 'blynk_token_here';

//Setup Gpio
var Gpio = require('pigpio').Gpio,
  motorF1 = new Gpio(ServoPinF1, {mode: Gpio.OUTPUT}),
  motorF2 = new Gpio(ServoPinF2, {mode: Gpio.OUTPUT}),
  motorF3 = new Gpio(ServoPinF3, {mode: Gpio.OUTPUT}),
  motorF4 = new Gpio(ServoPinF4, {mode: Gpio.OUTPUT}),
  motorF5 = new Gpio(ServoPinF5, {mode: Gpio.OUTPUT}),
  
  motorE1 = new Gpio(ServoPinE1, {mode: Gpio.OUTPUT}),
  motorE2 = new Gpio(ServoPinE2, {mode: Gpio.OUTPUT}),
  
  motorH1 = new Gpio(ServoPinH1, {mode: Gpio.OUTPUT}),
  
  LED = new Gpio(LEDPin, {mode: Gpio.OUTPUT}),

//Start Blynk
var Blynk = require('blynk-library');
var blynk = new Blynk.Blynk(blynkToken);

//VirtualPins
var v0 = new blynk.VirtualPin(0);
var v1 = new blynk.VirtualPin(1);
var v2 = new blynk.VirtualPin(2);
var v3 = new blynk.VirtualPin(3);
var v4 = new blynk.VirtualPin(4);

var v5 = new blynk.VirtualPin(5);
var v6 = new blynk.VirtualPin(6);

var v7 = new blynk.VirtualPin(7);

var v8 = new blynk.VirtuslPin(8);
var v9 = new blynk.VirtualPin(9);
var v10 = new blynk.VirtualPin(10);
var v11 = new blynk.VirtuslPin(11);

var v12 = new blynk.VirtualPin(12);
var v13 = new blynk.VirtualPin(13);
var v14 = new blynk.VirtualPin(14);
var v15 = new blynk.VirtualPin(15);
var v16 = new blynk.VirtualPin(16);
var v17 = new blynk.VirtualPin(17);
var v18 = new blynk.VirtualPin(18);
var v19 = new blynk.VirtualPin(19);
var v20 = new blynk.VirtualPin(20);
var v21 = new blynk.VirtualPin(21);
var v22 = new blynk.VirtualPin(22);
var v23 = new blynk.VirtualPin(23);
var v24 = new blynk.VirtualPin(24);
var v25 = new blynk.VirtualPin(25);
var v26 = new blynk.VirtualPin(26);
var v27 = new blynk.VirtualPin(27);
var v28 = new blynk.VirtualPin(28);
var v29 = new blynk.VirtualPin(29);
var v30 = new blynk.VirtualPin(30);
var v31 = new blynk.VirtualPin(31);
var v32 = new blynk.VirtualPin(32);
var v33 = new blynk.VirtualPin(33);
var v34 = new blynk.VirtualPin(34);
var v35 = new blynk.VirtualPin(35);
var v36 = new blynk.VirtualPin(36);
var v37 = new blynk.VirtualPin(37);
var v38 = new blynk.VirtualPin(38);
var v39 = new blynk.VirtualPin(39);
var v40 = new blynk.VirtualPin(40);
var v41 = new blynk.VirtualPin(41);
var v42 = new blynk.VirtualPin(42);
var v43 = new blynk.VirtualPin(43);
var v44 = new blynk.VirtualPin(44);
var v45 = new blynk.VirtualPin(45);
var v46 = new blynk.VirtualPin(46);
var v47 = new blynk.VirtualPin(47);



//Functions
var ms;
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


function SETUP(HundertAchtzig,Neunzig,Null){
	motorF1.servoWrite(HundertAchtzig);
	motorF2.servoWrite(HundertAchtzig);
	motorF3.servoWrite(HundertAchtzig);
	motorF4.servoWrite(HundertAchtzig);
	motorF5.servoWrite(HundertAchtzig);
	
	motorE1.servoWrite(Neunzig);
	motorE2.servoWrite(Neunzig);
	
	motorH1.servoWrite(Null);
	//Notiycation 
	blynk.notify("All Servos go to Startposition!");
}

function Modi1(HundertAchtzig,Neunzig,Null){
	motorF1.servoWrite(Null);
	sleep(1500);
	motorF1.servoWrite(HundertAchtzig);
	motorF2.servoWrite(Null);
	sleep(1500);
	motorF2.servoWrite(HundertAchtzig);
	motorF3.servoWrite(Null);
	sleep(1500);
	motorF3.servoWrite(HundertAchtzig);
	motorF4.servoWrite(Null);
	sleep(1500);
	motorF4.servoWrite(HundertAchtzig);
	motorF5.servoWrite(Null);
	sleep(1500);
	motorF5.servoWrite(HundertAchtzig);
	motorF1.servoWrite(Null);
	sleep(500);
	motorF2.servoWrite(Null);
	sleep(500);
	motorF3.servoWrite(Null);
	sleep(500);
	motorF4.servoWrite(Null);
	sleep(1000);
	motorF5.servoWrite(Null);
	sleep(2000);
	motorF1.servoWrite(HundertAchtzig);
	sleep(500);
	motorF2.servoWrite(HundertAchtzig);
	sleep(500);
	motorF3.servoWrite(HundertAchtzig);
	sleep(500);
	motorF4.servoWrite(HundertAchtzig);
	sleep(1000);
	motorF5.servoWrite(HundertAchtzig);
	}
function Modi2(HundertAchtzig,Neunzig,Null){
	
	motorE1.servoWrite(Neunzig);
	motorH1.servoWrite(Null);
	sleep (2000);
	motorH1.servoWrite(Neunzig);
	motorF1.servoWrite(Null);
	motorF2.servoWrite(Null);
	motorF3.servoWrite(Null);
	motorF4.servoWrite(Null);
	sleep (1500);
	motorF5.servoWrite(Null);
	sleep (5000);
	motorF5.servoWrite(HundertAchtzig);
	sleep(1500);
	motorF1.servoWrite(HundertAchtzig);
	motorF2.servoWrite(HundertAchtzig);
	motorF3.servoWrite(HundertAchtzig);
	motorF4.servoWrite(HundertAchtzig);	
	}
function Modi3(HundertAchtzig,Neunzig,Null){
	motorE1.servoWrite(HundertAchtzig);
	
	sleep (1000);
	motorE2.servoWrite(Null);
	sleep (4000);
	motorF1.servoWrite(Null);
	motorF2.servoWrite(Null);
	motorF3.servoWrite(Null);
	motorF4.servoWrite(Null);
	sleep (1500);
	motorF5.servoWrite(Null);
	sleep (1500);
	motorE1.servoWrite(Neunzig);
	motorE2.servoWrite(Neunzig);
	sleep (2000);
	motorH1.servoWrite(HundertAchtzig);
	sleep (1500);
	motorF5.servoWrite(HundertAchtzig);
	sleep(1500);
	motorF1.servoWrite(HundertAchtzig);
	motorF2.servoWrite(HundertAchtzig);
	motorF3.servoWrite(HundertAchtzig);
	motorF4.servoWrite(HundertAchtzig);
}
function Manuel(HundertAchtzig,Neunzig,Null){
v37.on('write', function(param){
	console.log('V37: ', param);
	while(param[0])==='1'){
	
	v0.on('write', function(param){
		console.log('VO: ', param);
		if (param [0]=== '0') {
			motorF1.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorF1.servoWrite(HundertAchtzig);}}
	v1.on('write', function(param){
		console.log('V1: ', param);
		if (param [0]=== '0') {
			motorF2.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorF2.servoWrite(HundertAchtzig);}}
	v2.on('write', function(param){
		console.log('V2: ', param);
		if (param [0]=== '0') {
			motorF2.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorF2.servoWrite(HundertAchtzig);}}
	v3.on('write', function(param){
		console.log('V3: ', param);
		if (param [0]=== '0') {
			motorF3.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorF3.servoWrite(HundertAchtzig);}}
	v4.on('write', function(param){
		console.log('V4: ', param);
		if (param [0]=== '0') {
			motorF4.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorF4.servoWrite(HundertAchtzig);}}
	v5.on('write', function(param){
		console.log('V5: ', param);
		if (param [0]=== '0') {
			motorE1.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorE1.servoWrite(Neunzig);}
		else if(param[0]=== '2'){
			motorE1.servoWrite(HundertAchtzig);}}
	v6.on('write', function(param){
		console.log('V6: ', param);
		if (param [0]=== '0') {
			motorE2.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorE2.servoWrite(Neunzig);}
		else if(param[0]=== '2'){
			motorE2.servoWrite(HundertAchtzig);}}
	v7.on('write', function(param){
		console.log('V7: ', param);
		if (param [0]=== '0') {
			motorH1.servoWrite(Null);}
		else if (param[0]=== '1') {
			motorH1.servoWrite(Neunzig);}
		else if(param[0]=== '2'){
			motorH1.servoWrite(HundertAchtzig);}}
	v36.on('write', function(param){
		console.log('V36: ', param);
		if (param [0]=== '0') {
		}
		else if (param[0]=== '1') {
			SETUP()
			param=0;}
		}
}
	else if (param[0])==='0'){
		
		break;
	}
		
	}}
function Morsecode(){} 
function Action1(){
	
}